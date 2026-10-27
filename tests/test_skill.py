from pathlib import Path
import importlib.util
import json
import re
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills/deep-learning-innovation-scout'
spec = importlib.util.spec_from_file_location('catalog_search', SKILL / 'scripts/search_catalog.py')
search_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(search_module)


class SkillTests(unittest.TestCase):
    def test_source_coverage_and_evidence_boundaries(self):
        data = json.loads((SKILL / 'references/catalog.json').read_text(encoding='utf-8'))
        records = data['records']
        self.assertEqual(len({r['id'] for r in records}), len(records))
        self.assertEqual({p for r in records for p in r['source_pages']}, set(range(1, 49)))
        self.assertTrue(any(r['evidence_status'] == 'quarantine' for r in records))
        self.assertTrue(all(r['tag_basis'] for r in records))

    def test_acronym_and_chinese_retrieval(self):
        for query in ['WTConv', '小波 大感受野']:
            result = search_module.search(query, limit=8)
            self.assertTrue(any('2407.05848' == x['arxiv_id'] for x in result), query)
        result = search_module.search('时序 周期 噪声', limit=20)
        self.assertTrue(any('TSLANet' in x['title'] for x in result))

    def test_quarantined_mismatch_is_not_recommended(self):
        normal = search_module.search('MDCR', limit=100)
        self.assertEqual(normal, [])
        audit = search_module.search('MDCR', limit=100, include_quarantined=True)
        self.assertTrue(audit)
        self.assertTrue(all(x['evidence_status'] == 'quarantine' for x in audit))

    def test_references_self_contained(self):
        for file in SKILL.rglob('*.md'):
            for target in re.findall(r'\]\(([^)]+)\)', file.read_text(encoding='utf-8')):
                if re.match(r'https?://|#', target):
                    continue
                resolved = (file.parent / target.split('#')[0]).resolve()
                self.assertTrue(resolved.is_relative_to(SKILL.resolve()), (file, target))
                self.assertTrue(resolved.exists(), (file, target))

    def test_install_and_repeat_without_overwriting(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            command = [sys.executable, str(ROOT / 'install.py'), '--target', 'both', '--codex-home', str(root / 'codex'), '--dsh-home', str(root / 'dsh'), '--agents-home', str(root / 'agents')]
            for _ in range(2):
                result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8')
                self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
            codex = root / 'codex/skills/deep-learning-innovation-scout'
            dsh = root / 'dsh/skills/deep-learning-innovation-scout'
            self.assertTrue((codex / 'SKILL.md').is_file())
            self.assertEqual((root / 'agents/skills/deep-learning-innovation-scout').resolve(), codex.resolve())
            original = (dsh / 'SKILL.md').read_bytes()
            (dsh / 'SKILL.md').write_bytes(original + b'\nlocal change\n')
            blocked = subprocess.run(command, capture_output=True, text=True, encoding='utf-8')
            self.assertNotEqual(blocked.returncode, 0)
            self.assertEqual((dsh / 'SKILL.md').read_bytes(), original + b'\nlocal change\n')

    def test_public_zip_excludes_private_material(self):
        archive = ROOT / 'dist/deep-learning-innovation-scout-v2.1.0.zip'
        with zipfile.ZipFile(archive) as z:
            names = z.namelist()
            self.assertTrue(any(n.endswith('/install.py') for n in names))
            self.assertTrue(any(n.endswith('/references/catalog.json') for n in names))
            self.assertFalse(any('/local-only/' in n or 'private-archive' in n or n.endswith('.pdf') for n in names))

    def test_new_library_retrieves_mechanism_and_real_interfaces(self):
        for query, title in [('RevIN', 'RevIN'), ('上采样', 'DySample'), ('GRN', 'GRN')]:
            result = search_module.search_library(query, kind='module', limit=6)
            self.assertTrue(any(r['title'] == title for r in result), query)
        records = search_module.all_records()
        grn = next(r for r in records if r['kind'] == 'code' and r['title'] == 'GRN.py')
        forward = next(m for c in grn['interfaces'] if c['name'] == 'GRN' for m in c['methods'] if m['name'] == 'forward')
        self.assertIn('x', forward['signature'])
        pconv = next(r for r in records if r['kind'] == 'code' and 'EnhancedPartialConv2d' in r.get('symbols', []))
        self.assertTrue(any('forward' in f['detail'] and '新建' in f['detail'] for f in pconv['static_findings']))
        self.assertFalse(any(r.get('runtime_verified') for r in records))

    def test_no_dangling_evidence_ids_and_dataset_coverage(self):
        records = search_module.all_records()
        ids = {r['id'] for r in records}
        self.assertEqual(len(ids), len(records))
        for r in records:
            for field in ['code_refs', 'paper_refs']:
                self.assertTrue(set(r.get(field, [])) <= ids, (r['id'], field))
        datasets = [r for r in records if r['kind'] == 'dataset']
        self.assertEqual(len(datasets), 95)
        self.assertEqual({r['id'] for r in datasets}, {f'DATA-{n:03d}' for n in range(1, 96)})
        self.assertTrue(all(r['source_doc'] in ids and r['source_pages'] for r in datasets))
        self.assertTrue(all('m6z.cn' not in u for r in datasets for u in r['primary_urls']))

    def test_corrected_module_does_not_reuse_quarantined_lead(self):
        result = search_module.search_library('MDCR', kind='module', limit=4)
        self.assertTrue(any(r['title'] == 'MDCR-HCF' for r in result))
        self.assertFalse(any(r['evidence_status'] == 'quarantine' for r in result))
        result = search_module.search_library('MDCR', kind='lead', limit=100)
        self.assertFalse(any(r['id'] == 'DLI-103' for r in result))

    def test_upgrade_keeps_local_archive_and_backup_outside_discovery(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            cmd = [sys.executable, str(ROOT / 'install.py'), '--target', 'dsh', '--dsh-home', str(root / 'dsh')]
            first = subprocess.run(cmd, capture_output=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            dest = root / 'dsh/skills/deep-learning-innovation-scout'
            private = dest / 'references/local-only/personal-note.txt'
            private.parent.mkdir(parents=True)
            private.write_text('keep private archive', encoding='utf-8')
            (dest / 'SKILL.md').write_text('previous version', encoding='utf-8')
            upgrade = subprocess.run(cmd + ['--upgrade'], capture_output=True)
            self.assertEqual(upgrade.returncode, 0, upgrade.stderr)
            self.assertEqual(private.read_text(encoding='utf-8'), 'keep private archive')
            self.assertEqual(len(list((root / 'dsh/skills').iterdir())), 1)
            backups = list((root / 'dsh/skill-backups').iterdir())
            self.assertEqual(len(backups), 1)
            self.assertEqual((backups[0] / 'SKILL.md').read_text(encoding='utf-8'), 'previous version')

    def test_release_has_no_collector_prose_or_private_paths(self):
        archive = ROOT / 'dist/deep-learning-innovation-scout-v2.1.0.zip'
        with zipfile.ZipFile(archive) as z:
            for name in z.namelist():
                if not name.endswith(('.md', '.json', '.yaml', '.py')):
                    continue
                content = z.read(name).decode('utf-8')
                private_markers = ['C:' + chr(92) + 'Users' + chr(92) + 'admin', 'D:' + chr(92) + 'workspace', '\u6df1\u5ea6\u4e4b\u773c', 'Lar' + 'ry\u540c\u5b66', 'Ai' + 'Himeragi']
                for private_marker in private_markers:
                    self.assertNotIn(private_marker, content, (name, private_marker))

    def test_material_inventory_accounts_for_all_files(self):
        coverage = json.loads((SKILL / 'references/material-coverage.json').read_text(encoding='utf-8'))['records']
        stats = json.loads((SKILL / 'references/coverage.json').read_text(encoding='utf-8'))
        self.assertEqual(sum(r['copies'] for r in coverage), stats['source_files'])
        self.assertEqual(len(coverage), stats['unique_file_hashes'])
        self.assertEqual(sum(r['copies'] for r in coverage if r['suffix'] == '.pdf'), stats['pdf_files'])
        papers = json.loads((SKILL / 'references/library/papers.json').read_text(encoding='utf-8'))['records']
        self.assertEqual(sum(r['pages'] for r in papers), stats['unique_pdf_pages'])
        self.assertTrue(all(r['status'] for r in coverage))

    def test_archival_never_executes_or_extracts_supplied_code(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / 'source'
            skill = root / 'skill'
            source.mkdir()
            skill.mkdir()
            (skill / 'SKILL.md').write_text('test skill', encoding='utf-8')
            (source / 'module.py').write_text('raise RuntimeError("must never execute source")', encoding='utf-8')
            (source / 'notes.txt').write_text('owned private notes', encoding='utf-8')
            with zipfile.ZipFile(source / 'sources.zip', 'w') as z:
                z.writestr('../../escape.py', 'raise RuntimeError("archive code must stay data")')
            result = subprocess.run([sys.executable, str(ROOT / 'tools/archive_materials.py'), '--source-dir', str(source), '--skill-dir', str(skill)], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertFalse((root / 'escape.py').exists())
            codes = json.loads((skill / 'references/local-only/code-source.json').read_text(encoding='utf-8'))
            self.assertEqual(len(codes), 2)
            self.assertTrue(any('must never execute' in r['text'] for r in codes.values()))

    def test_failure_word_beats_broad_domain_terms(self):
        result = search_module.search_library('医学分割 边界', kind='module', limit=5)
        self.assertEqual(result[0]['family'], 'boundary')

    def test_every_paper_has_a_scoped_research_note(self):
        records = search_module.all_records()
        ids = {r['id'] for r in records}
        for paper in [r for r in records if r['kind'] == 'paper']:
            self.assertTrue(paper['method_summary'])
            self.assertNotIn('尚无逐篇', paper['summary_basis'])
            self.assertTrue(set(paper['related_module_ids']) <= ids)

    def test_source_occurrences_are_accounted_without_inflating_methods(self):
        records = search_module.all_records()
        byid = {r['id']:r for r in records}
        sources = [r for r in records if r['kind']=='source']
        leads = [r for r in records if r['kind']=='lead']
        self.assertEqual(len(sources),363)
        self.assertEqual(sum(r['item_type']=='method_occurrence' for r in sources),361)
        self.assertEqual({p for r in sources for p in r['source_pages']},set(range(1,49)))
        for lead in leads:
            self.assertTrue(lead['source_occurrence_refs'])
            self.assertTrue(all(lead['id'] in byid[s]['lead_refs'] for s in lead['source_occurrence_refs']))
        for source in sources:
            if source['item_type']=='method_occurrence':self.assertTrue(source['lead_refs'])
            self.assertTrue(set(source['lead_refs'])<=set(byid))

    def test_corrected_neighbors_and_recovered_title_do_not_mix_sources(self):
        byid={r['id']:r for r in search_module.all_records()}
        self.assertEqual(byid['DLI-238']['arxiv_id'],None)
        self.assertFalse(any('2406.03751' in u for u in byid['DLI-238']['paper_urls']))
        self.assertFalse(any('2503.10622' in u for u in byid['DLI-239']['paper_urls']))
        self.assertEqual(byid['DLI-322']['title'],'Align Images Before You Generate')
        self.assertIn(28,byid['DLI-322']['source_pages'])

    def test_research_cards_show_reading_level_and_sources_stay_out_of_default_ranking(self):
        records=search_module.all_records();byid={r['id']:r for r in records}
        cards=[r for r in records if r['kind']=='research']
        self.assertEqual(len(cards),322)
        self.assertTrue(all(r['reading_level'] and r['lead_refs'] for r in cards))
        self.assertTrue(all(set(r['module_refs'])<=set(byid) for r in cards))
        self.assertTrue(any(not r['module_refs'] and '待核实' in r['mechanism_summary'] or not r['module_refs'] and '未写出' in r['mechanism_summary'] for r in cards))
        self.assertFalse(any(r['kind']=='source' for r in search_module.search_library('VideoFusion',limit=100)))
        self.assertTrue(search_module.search_library('VideoFusion',kind='source',limit=100))
        result=search_module.search_library('WTConv',kind='module')
        self.assertTrue(any(r['title']=='WTConv' and r['primary_urls'] and not r['runtime_verified'] for r in result))

    def test_new_identity_conflicts_are_excluded(self):
        for ident in ['DLI-010','DLI-152','DLI-158']:
            rows=search_module.search_library('',kind='lead',limit=1000)
            self.assertNotIn(ident,{r['id'] for r in rows})
            audit=search_module.search_library('',kind='lead',limit=1000,include_quarantined=True)
            self.assertIn(ident,{r['id'] for r in audit})


if __name__ == '__main__':
    unittest.main()

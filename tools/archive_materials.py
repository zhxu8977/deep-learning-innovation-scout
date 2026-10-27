"""Archive owned local PDF/source material as private data; never import supplied code."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import zipfile


def decode(raw):
    for encoding in ['utf-8-sig', 'gb18030', 'utf-16']:
        try:
            return raw.decode(encoding)
        except UnicodeError:
            pass
    return raw.decode('utf-8', errors='replace')


def save(file, value):
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-dir', type=Path, required=True)
    parser.add_argument('--skill-dir', type=Path, required=True)
    args = parser.parse_args()
    source = args.source_dir.resolve()
    target = args.skill_dir.resolve() / 'references/local-only'
    if not source.is_dir() or not (args.skill_dir / 'SKILL.md').is_file():
        parser.error('Supply an existing source directory and an installed skill directory')
    if target.is_relative_to(source):
        parser.error('Archive output must be outside source directory')
    target.mkdir(parents=True, exist_ok=True)
    code_file = target / 'code-source.json'
    codes = json.loads(code_file.read_text(encoding='utf-8')) if code_file.exists() else {}
    inventory = []
    try:
        from pypdf import PdfReader
    except ImportError:
        PdfReader = None
    supplemental = {}
    def add_code(raw, path):
        sha = hashlib.sha256(raw).hexdigest()
        ident = 'CODE-' + sha[:12]
        item = codes.setdefault(ident, {'sha256': sha, 'paths': [], 'text': decode(raw)})
        if path not in item['paths']:
            item['paths'].append(path)
    for file in sorted(source.rglob('*')):
        if not file.is_file() or file.is_symlink() or any(x in {'.git', '.idea', '__pycache__'} for x in file.relative_to(source).parts):
            continue
        relative = file.relative_to(source).as_posix()
        raw = file.read_bytes()
        sha = hashlib.sha256(raw).hexdigest()
        row = {'path': relative, 'sha256': sha, 'bytes': len(raw), 'status': 'indexed_only'}
        try:
            if file.suffix.lower() == '.pdf':
                if PdfReader is None:
                    row['status'] = 'needs_optional_pypdf'
                else:
                    reader = PdfReader(file)
                    pages = [{'page': n + 1, 'text': p.extract_text() or ''} for n,p in enumerate(reader.pages)]
                    save(target / 'documents' / ('DOC-' + sha[:12] + '.json'), {'sha256': sha, 'paths': [relative], 'pages': pages})
                    if file.name.startswith('366个') or file.name in {'AI工作流.pdf', 'AI寻找论文创新点的完整提示词工作流.pdf'}:
                        role = 'catalog' if file.name.startswith('366个') else 'workflow'
                        (target / (role + '-source.md')).write_text('\n\n'.join(f'## PDF 第 {p["page"]} 页\n\n{p["text"]}' for p in pages), encoding='utf-8')
                    row.update(status='pdf_text_archived', pages=len(pages))
            elif file.suffix.lower() == '.py':
                add_code(raw, relative)
                row['status'] = 'source_archived_as_data'
            elif file.suffix.lower() == '.zip':
                with zipfile.ZipFile(file) as archive:
                    members = []
                    for member in archive.infolist():
                        if member.is_dir():
                            continue
                        members.append({'path': member.filename, 'bytes': member.file_size})
                        if member.filename.endswith('.py') and member.file_size <= 2_000_000:
                            add_code(archive.read(member), relative + '::' + member.filename)
                    supplemental[sha] = {'paths': [relative], 'members': members}
                row['status'] = 'zip_members_and_source_indexed'
            elif file.suffix.lower() in {'.md', '.txt', '.json', '.yaml', '.yml'}:
                supplemental[sha] = {'paths': [relative], 'text': decode(raw)}
                row['status'] = 'text_archived'
            elif file.suffix.lower() in {'.docx', '.pptx'}:
                import xml.etree.ElementTree as ET
                with zipfile.ZipFile(file) as archive:
                    names = [n for n in archive.namelist() if n == 'word/document.xml' or re.fullmatch(r'ppt/slides/slide\d+\.xml', n)]
                    text = '\n'.join(' '.join(ET.fromstring(archive.read(n)).itertext()) for n in sorted(names))
                    supplemental[sha] = {'paths': [relative], 'text': text}
                row['status'] = 'office_xml_text_archived'
        except Exception as error:
            row.update(status='read_error', error=str(error))
        inventory.append(row)
    save(code_file, codes)
    save(target / 'user-import-supplemental.json', supplemental)
    save(target / 'user-import-inventory.json', inventory)
    counts = {}
    for row in inventory:
        counts[row['status']] = counts.get(row['status'], 0) + 1
    print(json.dumps({'private_archive': str(target), 'files': len(inventory), 'statuses': counts,
                      'note': 'Only private archival; Word screenshots/legacy documents and 7z need a separate reader. Public indexes are not silently rebuilt.'}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()

"""Offline retrieval over source-grounded bibliography; no third-party dependencies."""
from pathlib import Path
import argparse
import json
import re
import sys

ALIASES = {
    '医学': ['medical', 'biomedical', '医学分割'],
    '分割': ['segmentation'], '边界': ['boundary', 'edge', '边界/结构'],
    '模糊': ['boundary', 'restoration'], '小目标': ['small object', 'small target', '遥感/小目标'],
    '漏检': ['detection', 'small object'], '遥感': ['remote sensing', 'aerial', 'uav'],
    '红外': ['infrared'], '多模态': ['multimodal', 'multi-modal', '融合/对齐'],
    '融合': ['fusion'], '错位': ['alignment', 'registration'], '配准': ['registration', 'alignment'],
    '时序': ['time series', 'forecasting', '时间序列'], '时间序列': ['time series', 'forecasting'],
    '周期': ['frequency', 'spectral'], '频域': ['frequency', 'fourier', 'spectral'],
    '小波': ['wavelet'], '轻量': ['lightweight', 'efficient', 'mobile'],
    '慢': ['efficient', 'acceleration', 'cpu'], '显存': ['memory', 'efficient'],
    '跨域': ['domain', 'distribution', '归一化/分布偏移'], '泛化': ['generalization', 'domain'],
    '少样本': ['few-shot', 'in-context'], '弱监督': ['scribble', 'semi-supervised'],
    '少标注': ['scribble', 'semi-supervised', 'support-set'],
    '噪声': ['denoising', 'spectral'], '恢复': ['restoration'], '点云': ['point cloud'],
    '长序列': ['long-range', 'state space', 'mamba'], 'mamba': ['state space', 'mambaout'],
    '超分': ['super-resolution'], '大模型': ['language model', 'llm'],
    '压缩': ['compression', 'token reduction'], '不确定': ['uncertainty'],
    '大感受野': ['large receptive', 'global'],
}
CATALOG = Path(__file__).resolve().parents[1] / 'references/catalog.json'
LIBRARY = CATALOG.parent / 'library'
ALIASES.update({
    '断裂': ['boundary', 'topology', '连通', '边界'], '条带': ['strip', '条带'],
    '归一化': ['normalization', 'revin', 'grn'], '漂移': ['distribution shift', 'revin', '漂移'],
    '上采样': ['upsampling', 'dysample', 'featup', '上采样'],
    '下采样': ['downsampling', 'wavelet', 'hwd', '下采样'],
    '抖动': ['smoothnet', 'jitter', '抖动'], '脑电': ['eeg', 'cleegn', '脑电'],
    '工业': ['工业缺陷', 'industrial', 'defect'], '缺陷': ['defect', '工业缺陷'],
    '超声': ['ultrasound', 'haam', '超声'], '三维': ['volumetric', '3d', '体素'],
    '体数据': ['volumetric', '体素'], '融合错位': ['alignment', 'fusion', '配准'],
    '长尾': ['long-tail', 'imbalance', '少数类'], '不平衡': ['imbalance', '长尾'],
    '重参数': ['reparameterization', '折叠'], '部署': ['deploy', 'latency', '部署'],
    '数据集': ['dataset'], '医学分割': ['medical', 'segmentation', '医学', '分割'],
})


def all_records():
    records = []
    for name in ['modules', 'papers', 'code-interfaces', 'datasets', 'recipes', 'research-cards', 'source-items']:
        file = LIBRARY / (name + '.json')
        if file.exists():
            records.extend(json.loads(file.read_text(encoding='utf-8'))['records'])
    records.extend(dict(r, kind='lead') for r in json.loads(CATALOG.read_text(encoding='utf-8'))['records'])
    return records


def search_library(query, *, limit=8, include_quarantined=False, tag=None, kind=None, family=None):
    q = query.casefold().strip()
    terms = set(re.findall(r'[a-z0-9][a-z0-9_.+\-]*|[\u4e00-\u9fff]+', q))
    for key, values in ALIASES.items():
        if key in q:
            terms.update(v.casefold() for v in values)
    results = []
    for record in all_records():
        if record['kind']=='source' and kind!='source':
            continue
        if record.get('exclude_from_recommendation') and not include_quarantined:
            continue
        if kind and record['kind'] != kind:
            continue
        if family and record.get('family') != family:
            continue
        if record.get('evidence_status') in {'quarantine', 'parse_error'} and not include_quarantined:
            continue
        tags = record.get('tags', [])
        if tag and tag not in tags:
            continue
        names = [record['title']] + record.get('aliases', []) + record.get('symbols', [])
        title = ' '.join(names).casefold()
        detail_keys = ['mechanism', 'integration', 'risks', 'minimal_experiment', 'topic_label', 'method_summary',
                       'research_use', 'group', 'task', 'selection_notes', 'search_terms',
                       'failure', 'hypothesis', 'decision', 'source_categories', 'source_aliases',
                       'mechanism_summary', 'research_question', 'reading_level']
        detail = ' '.join(str(record.get(key, '')) for key in detail_keys).casefold()
        tag_text = ' '.join(tags).casefold()
        score = 0
        matches = []
        for term in terms:
            points = (10 if term in title else 0) + (3 if term in tag_text else 0) + (2 if term in detail else 0)
            if points:
                score += points
                matches.append(term)
        if q and not score:
            continue
        if q and any(q == n.casefold() for n in names):
            score += 100
        # Failure terms should outrank broad domain synonyms, e.g. "医学分割 边界"
        # must not be dominated by unrelated volumetric cards just for saying "medical".
        if record['kind'] == 'module':
            mechanism = record.get('mechanism', '')
            if '边界' in q or '断裂' in q:
                score += 30 if record.get('family') == 'boundary' else 0
                score += 18 if any(w in mechanism for w in ['边界', '细长', '细粒度空间']) else 0
            if '小目标' in q:
                score += 18 if any(w in mechanism for w in ['小目标', '细节']) else 0
            if '漂移' in q:
                score += 20 if record.get('family') == 'normalization' else 0
            if record.get('family') == 'volumetric' and not any(w in q for w in ['三维', '3d', '体数据', '体素', '切片']):
                score *= 0.65
        if score:
            score *= {'module': 1.8, 'recipe': 1.6, 'dataset': 1.0, 'paper': 0.8, 'guide': 0.5, 'code': 0.5, 'lead': 0.6, 'research': 1.1, 'source': 0.3}[record['kind']]
        results.append(dict(record, retrieval_score=round(score, 3), matched_terms=sorted(matches)))
    return sorted(results, key=lambda r: (-r['retrieval_score'], r['id']))[:limit]


def search(query, *, limit=8, include_quarantined=False, tag=None):
    data = json.loads(CATALOG.read_text(encoding='utf-8'))
    q = query.casefold()
    terms = set(re.findall(r'[a-z0-9][a-z0-9_.+\-]*|[\u4e00-\u9fff]+', q))
    for key, values in ALIASES.items():
        if key in q:
            terms.update(values)
    results = []
    for record in data['records']:
        if record['evidence_status'] == 'quarantine' and not include_quarantined:
            continue
        if tag and tag not in record['tags']:
            continue
        title = (record['title'] + ' ' + (record['verified_title'] or '')).casefold()
        tags = ' '.join(record['tags']).casefold()
        categories = ' '.join(record['source_categories']).casefold()
        aliases = ' '.join(record.get('source_aliases', []) + record['other_urls']).casefold()
        score = 0
        matches = []
        for term in terms:
            points = (5 if term in title else 0) + (2 if term in tags else 0) + (1 if term in categories else 0) + (3 if term in aliases else 0)
            if points:
                score += points
                matches.append(term)
        if query and not score:
            continue
        # A verified abstract is useful but cannot rescue an unrelated match.
        if score and record['evidence_status'] == 'verified_metadata':
            score += 0.25
        results.append(dict(record, retrieval_score=score, matched_terms=sorted(matches)))
    return sorted(results, key=lambda x: (-x['retrieval_score'], x['id']))[:limit]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('query', nargs='*')
    parser.add_argument('--limit', type=int, default=8)
    parser.add_argument('--tag')
    parser.add_argument('--kind', choices=['module', 'paper', 'guide', 'code', 'dataset', 'lead', 'recipe', 'research', 'source'])
    parser.add_argument('--family', help='机制族，例如 frequency / fusion / normalization')
    parser.add_argument('--stats', action='store_true')
    parser.add_argument('--inspect', metavar='ID')
    parser.add_argument('--include-quarantined', action='store_true')
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args()
    if args.stats:
        print((CATALOG.parent / 'coverage.json').read_text(encoding='utf-8'))
        return
    if args.limit < 1:
        parser.error('--limit must be positive')
    if args.inspect:
        records = all_records()
        result = [x for x in records if x['id'].casefold() == args.inspect.casefold()]
        if not result:
            parser.error('Unknown record ID')
    else:
        if not args.query and not args.tag and not args.family and not args.kind:
            parser.error('Provide a query, --kind, --family, --tag, --stats, or --inspect')
        result = search_library(' '.join(args.query), limit=args.limit, include_quarantined=args.include_quarantined, tag=args.tag, kind=args.kind, family=args.family)
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    if args.json:
        print(json.dumps({'query': ' '.join(args.query), 'count': len(result), 'records': result}, ensure_ascii=False, indent=2))
    else:
        print('检索分数只表示文字相关性，不代表效果、质量或创新性。')
        if not result:
            print('没有命中；换用机制词/英文同义词，或检查 source-audit.md。')
        for r in result:
            print(f'\n{r["id"]} | {r["kind"]} | {r["title"]}')
            print(f'  状态：{r["evidence_status"]}；分数：{r.get("retrieval_score", "精确ID") }')
            for key, label in [('reading_level','完成程度'),('mechanism_summary','关联机制'),('research_question','研究问题'),('controls','控制条件'),('simple_comparison','简单对照'),('next_reading','后续阅读'),('mechanism', '机制'), ('method_summary', '研究线索'), ('integration', '接入'), ('risks', '风险'), ('minimal_experiment', '最小实验'), ('task', '任务'), ('selection_notes', '选择依据'), ('failure', '失败现象'), ('hypothesis', '假设'), ('decision', '判定')]:
                if r.get(key):
                    print(f'  {label}：{r[key]}')
            if r.get('source_pages'):
                print(f'  来源页码：{r["source_pages"]}')
            urls = r.get('primary_urls', []) + r.get('paper_urls', [])
            if urls:
                print('  原始学术来源：' + ' ; '.join(urls))
            for note in r.get('quality_notes', []):
                print('  核对事项：' + note)
            if r.get('code_refs'):
                print('  关联代码ID：' + ', '.join(r['code_refs'][:6]) + '（--inspect 查看接口）')
            for finding in r.get('static_findings', []):
                print('  静态检查：' + finding['detail'])


if __name__ == '__main__':
    main()

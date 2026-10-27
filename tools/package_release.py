"""Build a public release with an allowlist; private archives and PDFs are excluded."""
from pathlib import Path
import hashlib
import json
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
NAME = 'deep-learning-innovation-scout'
SKILL = ROOT / 'skills' / NAME


def excluded(path):
    return any(p in {'local-only', 'private-archive', '__pycache__', '.git', '.venv', 'dist'} for p in path.parts) or path.suffix.lower() in {'.pdf', '.pyc', '.zip'}


def main():
    for name in ['LICENSE', 'NOTICE.md']:
        shutil.copy2(ROOT / name, SKILL / name)
    files = {}
    for file in sorted(SKILL.rglob('*')):
        relative = file.relative_to(SKILL)
        if file.is_symlink():
            raise RuntimeError(f'Unexpected symlink in source skill: {relative}')
        if file.is_file() and not excluded(relative) and relative.as_posix() != 'manifest.json':
            files[relative.as_posix()] = hashlib.sha256(file.read_bytes()).hexdigest()
    manifest = {'name': NAME, 'version': '2.0.0', 'files': files}
    (SKILL / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    allowed_files = {'README.md', 'NOTICE.md', 'LICENSE', '.gitignore', 'install.py'}
    allowed_dirs = {'skills', 'docs', 'tools', 'tests'}
    release_files = []
    for file in sorted(ROOT.rglob('*')):
        relative = file.relative_to(ROOT)
        if excluded(relative) or not file.is_file():
            continue
        if file.is_symlink():
            raise RuntimeError(f'Unexpected release symlink: {relative}')
        if relative.as_posix() in allowed_files or relative.parts[0] in allowed_dirs:
            release_files.append(file)
    dist = ROOT / 'dist'
    dist.mkdir(exist_ok=True)
    output = dist / (NAME + '-v2.0.0.zip')
    with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        for file in release_files:
            archive.write(file, arcname=NAME + '/' + file.relative_to(ROOT).as_posix())
    with zipfile.ZipFile(output) as archive:
        members = archive.namelist()
        if any('/local-only/' in p or p.lower().endswith('.pdf') or 'private-archive' in p for p in members):
            raise RuntimeError('Private material unexpectedly included in public archive')
    sha = hashlib.sha256(output.read_bytes()).hexdigest()
    (dist / (output.name + '.sha256')).write_text(sha + '  ' + output.name + '\n', encoding='utf-8')
    print(json.dumps({'zip': str(output), 'files': len(release_files), 'sha256': sha, 'skill_files': len(files)}, ensure_ascii=True, indent=2))


if __name__ == '__main__':
    main()

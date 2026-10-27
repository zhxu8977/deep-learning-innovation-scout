"""Install this local skill into Codex and/or DSH without network or dependencies."""
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import os
import shutil
import sys
import tempfile

NAME = 'deep-learning-innovation-scout'
SOURCE = Path(__file__).resolve().parent / 'skills' / NAME


def digest(file):
    return hashlib.sha256(file.read_bytes()).hexdigest()


def contained(candidate, root):
    resolved = candidate.resolve()
    if not resolved.is_relative_to(root.resolve()) or resolved == root.resolve():
        raise RuntimeError(f'Path escapes intended skills directory: {candidate}')


def verify_source():
    manifest = json.loads((SOURCE / 'manifest.json').read_text(encoding='utf-8'))
    for relative, expected in manifest['files'].items():
        file = SOURCE / relative
        contained(file, SOURCE)
        if not file.is_file() or digest(file) != expected:
            raise RuntimeError(f'Skill package integrity check failed: {relative}')
    return manifest


def install_into(home, *, upgrade, manifest):
    skill_root = home.expanduser().resolve() / 'skills'
    skill_root.mkdir(parents=True, exist_ok=True)
    dest = skill_root / NAME
    contained(dest, skill_root)
    if dest.exists():
        same = all((dest / p).is_file() and digest(dest / p) == sha for p, sha in manifest['files'].items())
        if same:
            print(f'Already installed and identical: {dest}')
            return dest
        if not upgrade:
            raise RuntimeError(f'Existing skill differs: {dest}. Use --upgrade to back it up before replacement.')
        if dest.is_symlink() or getattr(dest, 'is_junction', lambda: False)():
            raise RuntimeError('Refusing to replace a linked skill directory; inspect its target first.')
    stage = Path(tempfile.mkdtemp(prefix='.' + NAME + '-stage-', dir=skill_root))
    contained(stage, skill_root)
    # Preserve an incomplete staging directory on failure for inspection; never delete existing skills.
    shutil.copytree(SOURCE, stage, dirs_exist_ok=True, ignore=shutil.ignore_patterns('local-only', '__pycache__', '*.pyc'))
    # User-owned full texts stay local and survive an upgrade.
    local_archive = dest / 'references' / 'local-only'
    if local_archive.is_dir():
        shutil.copytree(local_archive, stage / 'references' / 'local-only', dirs_exist_ok=True)
    for relative, expected in manifest['files'].items():
        if digest(stage / relative) != expected:
            raise RuntimeError(f'Staged file mismatch: {relative}; inspect {stage}')
    if dest.exists():
        backup_root = home.expanduser().resolve() / 'skill-backups'
        backup_root.mkdir(exist_ok=True)
        backup = backup_root / (NAME + '-' + datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f'))
        contained(backup, backup_root)
        dest.rename(backup)
        print(f'Previous version backed up: {backup}')
    stage.rename(dest)
    print(f'Installed: {dest}')
    return dest


def discovery_link(dest, agents_home):
    skills = agents_home.expanduser().resolve() / 'skills'
    skills.mkdir(parents=True, exist_ok=True)
    link = skills / NAME
    if link.exists() or link.is_symlink():
        if link.resolve() != dest.resolve():
            raise RuntimeError(f'Existing discovery location points elsewhere; preserved: {link}')
        print(f'Discovery link already correct: {link}')
        return
    if os.name == 'nt':
        # CPython Windows junction support avoids requiring symlink privileges or running a shell.
        import _winapi
        _winapi.CreateJunction(str(dest), str(link))
    else:
        link.symlink_to(dest, target_is_directory=True)
    if link.resolve() != dest.resolve():
        raise RuntimeError(f'Discovery link verification failed: {link}')
    print(f'Discovery link: {link} -> {dest}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target', choices=['codex', 'dsh', 'both'], default='codex')
    parser.add_argument('--codex-home', type=Path, default=Path(os.environ.get('CODEX_HOME', str(Path.home() / '.codex'))))
    parser.add_argument('--dsh-home', type=Path, default=Path(os.environ.get('DSH_HOME', str(Path.home() / '.dsh'))))
    parser.add_argument('--agents-home', type=Path, default=Path.home() / '.agents')
    parser.add_argument('--upgrade', action='store_true')
    args = parser.parse_args()
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    manifest = verify_source()
    # Preflight discovery before making any installation changes.
    discovery = args.agents_home.expanduser().resolve() / 'skills' / NAME
    expected_codex = args.codex_home.expanduser().resolve() / 'skills' / NAME
    if args.target in ['codex', 'both'] and (discovery.exists() or discovery.is_symlink()) and discovery.resolve() != expected_codex.resolve():
        raise RuntimeError(f'Discovery path occupied; preserved: {discovery}')
    if args.target in ['codex', 'both']:
        dest = install_into(args.codex_home, upgrade=args.upgrade, manifest=manifest)
        discovery_link(dest, args.agents_home)
    if args.target in ['dsh', 'both']:
        install_into(args.dsh_home, upgrade=args.upgrade, manifest=manifest)
    print('Installation complete. Available from the next conversation turn; refresh/restart the client if it is not discovered.')


if __name__ == '__main__':
    try:
        main()
    except (OSError, RuntimeError, ValueError) as error:
        print(f'Installation stopped: {error}', file=sys.stderr)
        raise SystemExit(1)

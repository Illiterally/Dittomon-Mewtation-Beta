"""Fail when the player-facing release and its downloadable package disagree."""
import argparse
import hashlib
import io
import json
from pathlib import Path
import re
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[2]
PUBLIC = 'https://github.com/Illiterally/Dittomon-Mewtation-Beta'
API = 'https://api.github.com/repos/Illiterally/Dittomon-Mewtation-Beta'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Dittomon-download-check', 'Cache-Control': 'no-cache'})
    with urllib.request.urlopen(req, timeout=90) as response:
        return response.read()


def check_copy(text, release):
    expected = {release['archive'], release['patch'], release['root_download'], 'Dittomon' + release['version'] + '.gba'}
    found = set(re.findall(r'(?:PLAY-HERE_)?Dittomon[A-Za-z0-9_.-]+\.(?:zip|bps|gba)', text))
    require(found <= expected, 'Stale download filename(s): ' + ', '.join(sorted(found - expected)))


def check_repository(root, release):
    allowed = {'.git', '.github', 'assets', 'credits', 'docs', 'README.md', 'CREDITS.md', release['root_download']}
    require({p.name for p in root.iterdir()} <= allowed, 'Unexpected root files: retain only the current PLAY-HERE ZIP and supporting documents')
    download = root / release['root_download']
    require(download.is_file(), 'The current PLAY-HERE ZIP must be visible in the root file list')
    require(sha(download.read_bytes()) == release['assets'][release['archive']]['sha256'], 'Root PLAY-HERE ZIP differs from the current release download')
    for folder in ['assets', 'credits', 'docs']:
        require(not any(p.suffix.lower() in {'.bps', '.zip', '.gba', '.sav'} for p in (root / folder).rglob('*')), 'Download or private game file committed outside Releases')
    readme = (root / 'README.md').read_text(encoding='utf-8')
    require(readme.startswith('# Dittomon' + release['version'] + '\n'), 'README title differs from release')
    require('Public Beta' in '\n'.join(readme.splitlines()[:7]), 'Prominent Public Beta label is missing')
    require('PLAY HERE' in readme.splitlines()[2], 'Prominent PLAY HERE download link is missing')
    links = re.findall(r'\]\(([^)]+)\)', readme)
    require(links[0] == release['download'], 'First README link must download the current ZIP')
    require(release['download'] == PUBLIC + '/releases/download/' + release['tag'] + '/' + release['archive'], 'Download URL disagrees with release identity')
    require(release['tag'] == 'v' + release['version'], 'Tag/version mismatch')
    check_copy(readme, release)
    for path in [root / 'README.md', root / 'CREDITS.md', *(root / 'docs').glob('*.md')]:
        for link in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
            if ':' not in link and not link.startswith('#'):
                require((path.parent / link.split('#')[0]).exists(), 'Broken local link: ' + str(path) + ' -> ' + link)


def check_package(data, release):
    require(sha(data) == release['assets'][release['archive']]['sha256'], 'ZIP checksum differs from reviewed release')
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        require(z.testzip() is None, 'Damaged ZIP')
        files = {name: z.read(name) for name in z.namelist()}
    require([n for n in files if n.endswith('.bps')] == [release['patch']], 'Package must contain exactly the current patch')
    require(not any(n.lower().endswith(('.gba', '.sav', '.ss0', '.ss1')) for n in files), 'Private ROM/save in package')
    require(sha(files[release['patch']]) == release['assets'][release['patch']]['sha256'], 'Patch hash mismatch')
    info = json.loads(files['PATCH_INFO.json'])
    require(info['release']['version'] == release['version'] and info['release']['tag'] == release['tag'], 'Packaged version mismatch')
    require(info['patch']['file'] == release['patch'] and info['patch']['sha256'] == sha(files[release['patch']]), 'Patch metadata mismatch')
    require(info['result']['sha256'] == release['rom_sha256'], 'Result ROM identity mismatch')
    checksums = dict(line.split('  ', 1)[::-1] for line in files['SHA256SUMS.txt'].decode().splitlines())
    require(set(checksums) == set(files) - {'SHA256SUMS.txt'}, 'Incomplete package checksum coverage')
    require(all(sha(files[n]) == digest for n, digest in checksums.items()), 'Invalid packaged checksum')
    for name in ['README.txt', 'RELEASE_NOTES.txt']:
        check_copy(files[name].decode('utf-8'), release)
    require(release['patch'] in files['README.txt'].decode(), 'Setup instructions omit the current patch')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', type=Path, help='Check a prepared ZIP before upload')
    ap.add_argument('--live', action='store_true', help='Also verify Releases, public assets and website links')
    args = ap.parse_args()
    release = json.loads((ROOT / '.github/current-release.json').read_text())
    check_repository(ROOT, release)
    if args.package:
        check_package(args.package.read_bytes(), release)
    if args.live:
        root_data = fetch('https://raw.githubusercontent.com/Illiterally/Dittomon-Mewtation-Beta/main/' + release['root_download'])
        require(sha(root_data) == release['assets'][release['archive']]['sha256'], 'Public PLAY-HERE file differs from the current ZIP')
        current = json.loads(fetch(API + '/releases/latest'))
        require(current['tag_name'] == release['tag'] and not current['draft'], 'Latest GitHub release is wrong')
        require(release['download'] in current['body'], 'Release page lacks a direct ZIP download')
        check_copy(current['body'], release)
        require(set(a['name'] for a in current['assets']) == set(release['assets']), 'Unexpected/missing release assets')
        for asset in current['assets']:
            data = fetch(asset['browser_download_url'])
            require(sha(data) == release['assets'][asset['name']]['sha256'], 'Public asset checksum mismatch: ' + asset['name'])
            if asset['name'] == release['archive']:
                check_package(data, release)
        for route in ['/', '/projects/dittomon']:
            html = fetch('https://illiterally.wtf' + route).decode('utf-8')
            require(release['download'] in html and release['version'] + ' · Public Beta' in html, 'Website version/download mismatch: ' + route)
            check_copy(html, release)
    print('PASS: download layout, release identity, links' + (', package' if args.package or args.live else '') + (', and live delivery' if args.live else ''))


if __name__ == '__main__':
    main()

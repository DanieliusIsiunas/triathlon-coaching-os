#!/usr/bin/env python3
"""Validate known structural invariants. Does not validate coaching judgment."""
from pathlib import Path
import argparse
import re
import sys

def validate(root):
    errors, warnings = [], []
    def check(ok, message):
        if not ok:
            errors.append(message)
    manifest_path = root / 'knowledge/00-Coaching-OS-Manifest.md'
    if not manifest_path.is_file():
        return ['Missing canonical manifest'], []
    manifest = manifest_path.read_text()
    owned = re.findall(r'^\| `([^`]+)` \|', manifest, re.M)
    check(bool(owned), 'Manifest ownership table is missing')
    for path in owned:
        check((root/path).exists(), f'Owned path missing: {path}')
    markdown = sorted(root.rglob('*.md'))
    versions = []
    for path in markdown:
        text = path.read_text()
        rel = path.relative_to(root).as_posix()
        versions += [(rel, v) for v in re.findall(r'^System version: (.+)$', text, re.M)]
        for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
            target = link.split('#')[0]
            if not target or re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', target):
                continue
            check((path.parent/target).exists(), f'Broken link in {rel}: {target}')
        # Root-relative canonical paths are deliberately expressed in backticks.
        for target in re.findall(r'`((?:knowledge|templates|reviews|scripts|tests)/[^`]+)`', text):
            check((root/target).exists(), f'Broken canonical reference in {rel}: {target}')
        check(not re.search(r'^(?:<<<<<<<|=======|>>>>>>>)', text, re.M), f'Merge conflict in {rel}')
        if rel.startswith('knowledge/'):
            check(bool(re.search(r'^Last updated: \d{4}-\d{2}-\d{2}$', text, re.M)), f'Missing date: {rel}')
    check(len(versions)==1 and versions[0][0]=='knowledge/00-Coaching-OS-Manifest.md',
          'System version must be declared only in the canonical manifest')
    pointer = root/'00-Coaching-OS-Manifest.md'
    check(pointer.is_file() and 'knowledge/00-Coaching-OS-Manifest.md' in pointer.read_text(), 'Root manifest pointer is invalid')
    for name, budget in [('00-Coaching-OS-Manifest.md',120), ('PROJECT-INSTRUCTIONS.md',220)]:
        p=root/name
        check(p.is_file() and len(p.read_text().split())<=budget, f'Entry point is missing or no longer thin: {name}')
    active=root/'knowledge/03-Active-State.md'
    if active.exists():
        text=active.read_text()
        check(len(re.findall(r'^## Current block contract$',text,re.M))==1,
              'Active State must contain exactly one current block contract')
        contract_status=re.search(r'^- \*\*Status:\*\* (inactive|active|review due|reviewed pending replacement)\.?$',text,re.M)
        check(bool(contract_status),'Current block contract status is missing or invalid')
        check(not re.search(r'(?:average heart rate|training load|SWOLF|aerobic training effect)\s*(?:was|of|:)?\s*\d',text,re.I), 'Daily telemetry found in Active State')
        check(not re.search(r'\d{4}-\d{2}-\d{2}.*(?:bpm|strokes/min)',text), 'Dated sensor values found in Active State')
        if len(text.split())>900:
            warnings.append('Active State exceeds 900 words; check for completed sessions or duplicated policy')
    rules=root/'knowledge/04-Coach-Rules.md'
    if rules.exists():
        check('## Block contract and closure' in rules.read_text(),
              'Coach Rules is missing block contract and closure policy')
    weekly=root/'templates/weekly-review.md'
    if weekly.exists():
        check('## Block review mode - only when due' in weekly.read_text(),
              'Weekly template is missing due block-review mode')
    log=root/'knowledge/05-Learning-Log.md'
    if log.exists():
        text=log.read_text()
        fields=['Question/hypothesis','Evidence and alternatives','Intervention/decision',
                'Expected result and revision criterion','Review trigger','Status/outcome','Confidence']
        entries=re.split(r'^### ',text,flags=re.M)[1:]
        check(bool(entries), 'Learning Log has no structured entries')
        check('## Active investigations' in text and '## Retained learning' in text, 'Learning Log sections are missing')
        ids=[]
        for entry in entries:
            title=entry.splitlines()[0]
            ids.append(title.split(' - ')[0])
            for field in fields:
                check(f'- {field}:' in entry,f'Missing {field} in {title}')
            check(bool(re.search(r'- Status/outcome: (?:unresolved|supported|weakened|retired)\b',entry)), f'Invalid status in {title}')
        check(len(ids)==len(set(ids)), 'Duplicate learning identifiers')
        active_entries=text.split('## Active investigations',1)[-1].split('## Retained learning',1)[0]
        check(len(re.findall(r'^### ',active_entries,re.M))<=2, 'More than two active investigations')
    legacy=[p.relative_to(root).as_posix() for p in markdown if re.search(r'(?:State-\d|Instructions-Patch|backup|copy)',p.name,re.I)]
    check(not legacy, 'Possible duplicate/patch state files: '+', '.join(legacy))
    return errors,warnings

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    args=parser.parse_args()
    errors,warnings=validate(args.root)
    for message in warnings:
        print('WARNING:',message)
    for message in errors:
        print('ERROR:',message)
    print(f'{len(errors)} structural errors; {len(warnings)} size warnings. Coaching judgment not tested.')
    sys.exit(bool(errors))

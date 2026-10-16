#!/usr/bin/env python3
"""Reproduce the finite checks; this is not a verifier of the whole manuscript."""
from pathlib import Path
import re
import subprocess
import sys
import sympy

root = Path(__file__).resolve().parent
print('Python:', sys.version.split()[0], flush=True)
print('SymPy:', sympy.__version__, flush=True)

def run(args, cwd=root):
    print('\nRUN', ' '.join(args), flush=True)
    result = subprocess.run(args, cwd=cwd, text=True, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, check=False)
    print(result.stdout, end='', flush=True)
    if result.returncode:
        raise SystemExit(result.returncode)
    if 'sorryAx' in result.stdout:
        raise SystemExit('Unexpected proof placeholder in Lean dependencies')

for filename in ('DefectCore.lean', 'DualModel.lean'):
    source = (root / 'lean' / filename).read_text()
    # These two sources contain no nested comments. Strip comments before scanning.
    source = re.sub(r'/\-.*?\-/', '', source, flags=re.S)
    source = re.sub(r'--[^\n]*', '', source)
    if re.search(r'\b(sorry|admit|axiom)\b', source):
        raise SystemExit('Unexpected proof placeholder or axiom declaration: ' + filename)
print('PASS no proof placeholders or added axiom declarations', flush=True)
run([sys.executable, 'checks.py'])
run([sys.executable, 'scalar_checks.py'])
run(['lake', 'build'], root / 'lean')
run(['lake', 'env', 'lean', 'Audit.lean'], root / 'lean')
print('\nAll finite symbolic and Lean checks passed.', flush=True)

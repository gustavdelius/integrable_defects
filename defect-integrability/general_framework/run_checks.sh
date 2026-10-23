#!/usr/bin/env bash
# Run every check of the general framework and write verification.txt.
# Usage (from this directory): ./run_checks.sh
# The whole run takes about half an hour.
set -u
cd "$(dirname "$0")"
out="$PWD/verification.txt"
{
  echo "# Verification record for defect-integrability/general_framework"
  echo "# date: $(date -u +%Y-%m-%dT%H:%MZ)  commit: $(git rev-parse --short HEAD)"
  echo "# python: $(python3 --version 2>&1)  sympy: $(python3 -c 'import sympy; print(sympy.__version__)')"
  echo
  cd checks
  for s in check_balance.py check_tangency.py check_kinematics.py check_symbols.py check_scope.py check_type1_family.py check_guide_example.py; do
    echo "== $s"
    python3 -u "$s" 2>&1
  done
  for m in kdv:6 sg:5 nls:3 mkdv:6 bsq:5 tz:3; do
    echo "== check_hierarchy.py $m"
    python3 -u check_hierarchy.py "$m" 2>&1
  done
  cd ../lean
  echo "== lake build"
  lake build 2>&1 | tail -1
  echo "== lake env lean Audit.lean"
  lake env lean Audit.lean 2>&1
  echo "== placeholder scan"
  grep -rn "sorry\|^axiom" GeneralFramework/ || echo "no sorry, no added axioms"
} > "$out"
echo "PASS lines: $(grep -c '^PASS' "$out"); FAIL lines: $(grep -c '^FAIL' "$out")"

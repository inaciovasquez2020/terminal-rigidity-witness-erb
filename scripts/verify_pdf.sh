#!/usr/bin/env bash
set -euo pipefail

OUT="trw-erb-sigc.pdf"
LOCK="trw-erb-sigc.pdf.sha256"

test -f "$OUT"
test -f "$LOCK"

ACTUAL="$(shasum -a 256 "$OUT" | awk '{print $1}')"
EXPECTED="$(cat "$LOCK" | tr -d '[:space:]')"

if [[ "$ACTUAL" != "$EXPECTED" ]]; then
  echo "ERROR: pdf sha256 mismatch"
  echo "expected: $EXPECTED"
  echo "actual:   $ACTUAL"
  exit 1
fi

echo "OK: pdf sha256 matches lockfile"

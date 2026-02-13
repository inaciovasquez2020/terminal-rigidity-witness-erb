#!/usr/bin/env bash
set -euo pipefail

TEX="trw-erb-sigc.tex"
OUT="trw-erb-sigc.pdf"

latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error "$TEX" >/dev/null
test -f "$OUT"
echo "OK: built $OUT"

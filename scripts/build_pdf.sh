#!/usr/bin/env bash
set -euo pipefail

TEX="trw-erb-sigc.tex"
OUT="trw-erb-sigc.pdf"

# Clean previous artifacts (important in CI)
latexmk -C

# Build with full logs visible
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error "$TEX"

test -f "$OUT"
echo "OK: built $OUT"

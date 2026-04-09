# Scope Integrity Note (2026-04)

## Status
Conditional.

## Repository-compatible boundary
This repository is minimal and frozen in scope.
It contains:
1. the canonical ERB statement and analysis;
2. the canonical PDF/TEX source;
3. formal status metadata;
4. citation metadata.

It does not contain:
1. downstream implementations;
2. generalizations;
3. extensions beyond the stated SIGC assumptions;
4. an executable verifier.

## Weakest structural extension
Let
\[
\mathcal A_{\mathrm{SIGC}}
\]
denote the SIGC assumption set stated in the paper.

Let
\[
\mathrm{ERB}
\]
denote the terminal rigidity witness defined in the canonical manuscript.

For any downstream use
\[
U,
\]
the minimal admissibility condition is:
\[
U \text{ may invoke } \mathrm{ERB}
\Longrightarrow
U \text{ explicitly preserves } \mathcal A_{\mathrm{SIGC}}.
\]

## Minimal next artifact
The weakest next artifact is an executable downstream-scope audit emitting:
1. downstream uses of ERB that omit SIGC assumptions;
2. downstream uses that silently strengthen the ERB conclusion;
3. downstream uses that treat the repository as an implementation module;
4. downstream uses that claim extensions not present in the canonical paper.

## Label
This note is CONDITIONAL.
It preserves the repository's minimal frozen scope and paper-centered boundary.

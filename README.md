# Terminal Rigidity Witness (ERB)

Executable Rigidity Bound (ERB) witnesses for terminal rigidity.

A terminal rigidity witness certifies that a configuration admits **no admissible escape transformation**
under bounded locality and capacity constraints.

Formally, a witness W verifies

R(X) = True

where X is a terminal configuration satisfying

1. Local admissibility constraints
2. Capacity bounds
3. No escape morphism

The witness therefore proves that the system is **terminally rigid**.

## Witness Structure

A rigidity witness consists of

W = (C, B, V)

C  configuration  
B  capacity bound  
V  verification procedure

The witness verifies

¬∃ T : X → Y

such that T preserves locality constraints and capacity bounds.

## Repository Structure

src/
core witness verification code

docs/
formal witness definitions

proofs/
example rigidity certificates

tests/
verification tests

examples/
demonstration witnesses

## Conditional note
- `docs/SCOPE_INTEGRITY_NOTE_2026_04.md` — conditional note specifying the weakest downstream-scope audit compatible with the repository's minimal frozen scope.

## Lean proof portfolio classification

This repository is governed by [`docs/status/LEAN_PROOF_PORTFOLIO_CLASSIFICATION.md`](docs/status/LEAN_PROOF_PORTFOLIO_CLASSIFICATION.md). Its role in the portfolio is explicitly classified as proof-facing, conditional frontier, infrastructure/documentation, or legacy/scaffold.

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

## External status

This repository is governed by [`docs/status/EXTERNAL_STATUS_LOCK.md`](docs/status/EXTERNAL_STATUS_LOCK.md). Build success, CI success, dashboards, ledgers, axioms, admits, `sorry`, or placeholder witnesses do not constitute theorem-level closure.

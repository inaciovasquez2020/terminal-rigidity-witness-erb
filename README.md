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

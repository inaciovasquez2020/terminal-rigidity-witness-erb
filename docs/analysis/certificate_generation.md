# Certificate Generation

Given

X configuration  
B capacity bound  
T transform space

Algorithm

1. For each τ ∈ T
2. Evaluate τ(X)
3. If τ(X) ≠ X → escape exists
4. Otherwise add τ to certificate

If all transforms preserve X then

C = (X, B, T_checked)

is a valid rigidity certificate.

# Rigidity Certificate File Format

Certificates are stored as JSON objects.

Example

{
  "config": [1,2,3],
  "capacity": 5,
  "transforms_checked": ["identity"]
}

Verification rule

1. |config| ≤ capacity
2. ∀ transform τ in transforms_checked : τ(config) = config

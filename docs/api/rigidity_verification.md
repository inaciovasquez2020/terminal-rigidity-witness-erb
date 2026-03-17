# Rigidity Verification API

## is_terminally_rigid(config, capacity, transform_space)

Determines whether a configuration is terminally rigid.

Parameters
- config: configuration object
- capacity: maximum allowed size
- transform_space: iterable of admissible transformations

Returns
True if no admissible escape transformation exists.

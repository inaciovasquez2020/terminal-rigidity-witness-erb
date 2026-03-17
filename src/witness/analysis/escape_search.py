def find_escape(config, transform_space):
    """
    Search for an admissible escape transformation.
    transform_space: iterable of transformation functions.
    """
    for T in transform_space:
        new_config = T(config)
        if new_config != config:
            return T
    return None

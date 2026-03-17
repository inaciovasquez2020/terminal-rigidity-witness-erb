from .escape_search import find_escape

def is_terminally_rigid(config, capacity, transform_space):
    if len(config) > capacity:
        return False
    escape = find_escape(config, transform_space)
    return escape is None

from .constraints import capacity_ok, locality_ok

def verify_terminal(config, capacity):
    if not capacity_ok(config, capacity):
        return False
    if not locality_ok(config):
        return False
    return True

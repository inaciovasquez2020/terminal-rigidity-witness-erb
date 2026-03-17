from src.witness.cert.certificate import RigidityCertificate

def generate_certificate(config, capacity, transform_space):
    """
    Attempt to construct a rigidity certificate by verifying
    that no transform in transform_space changes the configuration.
    """
    checked = []
    for T in transform_space:
        if T(config) != config:
            return None
        checked.append(T)

    return RigidityCertificate(config, capacity, checked)

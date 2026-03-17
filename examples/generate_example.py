from src.witness.search.generate_certificate import generate_certificate
from src.witness.search.transform_library import identity, rotate_left

config = [1,2,3]
capacity = 5

cert = generate_certificate(config, capacity, [identity])

if cert:
    print("Certificate generated:", cert.config)
else:
    print("Configuration not rigid")

import json
from .certificate import RigidityCertificate

def save_certificate(cert, path):
    data = {
        "config": cert.config,
        "capacity": cert.capacity,
        "transforms_checked": [t.__name__ for t in cert.transforms_checked],
    }
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def load_certificate(path, transform_registry):
    with open(path) as f:
        data = json.load(f)
    transforms = [transform_registry[name] for name in data["transforms_checked"]]
    return RigidityCertificate(data["config"], data["capacity"], transforms)

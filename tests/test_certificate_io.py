import tempfile
from src.witness.cert.certificate import RigidityCertificate
from src.witness.cert.serializer import save_certificate, load_certificate

def identity(x):
    return x

def test_roundtrip():
    cert = RigidityCertificate([1,2,3], 5, [identity])

    with tempfile.NamedTemporaryFile() as f:
        save_certificate(cert, f.name)
        loaded = load_certificate(f.name, {"identity": identity})
        assert loaded.validate()

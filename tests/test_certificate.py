from src.witness.cert.certificate import RigidityCertificate

def identity(x):
    return x

def test_certificate_valid():
    cert = RigidityCertificate([1,2,3], 5, [identity])
    assert cert.validate()

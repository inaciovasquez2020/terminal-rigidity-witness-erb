from src.witness.search.generate_certificate import generate_certificate
from src.witness.search.transform_library import identity, append_zero

def test_generation_success():
    cert = generate_certificate([1,2,3], 5, [identity])
    assert cert is not None
    assert cert.validate()

def test_generation_fail():
    cert = generate_certificate([1,2,3], 5, [identity, append_zero])
    assert cert is None

from src.witness.analysis.rigidity import is_terminally_rigid

def identity(x):
    return x

def expand(x):
    return x + [0]

def test_rigid():
    assert is_terminally_rigid([1,2,3], 5, [identity])

def test_not_rigid():
    assert not is_terminally_rigid([1,2,3], 5, [identity, expand])

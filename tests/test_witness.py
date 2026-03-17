from src.witness.witness import TerminalRigidityWitness
from src.witness.verifier import verify_terminal

def test_witness():
    config = [1,2,3]
    w = TerminalRigidityWitness(config, 5, verify_terminal)
    assert w.verify()

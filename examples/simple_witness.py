from src.witness.witness import TerminalRigidityWitness
from src.witness.verifier import verify_terminal

config = [1,2,3]
capacity = 5

w = TerminalRigidityWitness(config, capacity, verify_terminal)

print("Witness verified:", w.verify())

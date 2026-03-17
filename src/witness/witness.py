class TerminalRigidityWitness:
    def __init__(self, config, capacity, verifier):
        self.config = config
        self.capacity = capacity
        self.verifier = verifier

    def verify(self):
        return self.verifier(self.config, self.capacity)

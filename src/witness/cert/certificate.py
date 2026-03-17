class RigidityCertificate:
    """
    Finite certificate proving terminal rigidity.

    Fields
    ------
    config: configuration under verification
    capacity: capacity bound
    transforms_checked: list of transformations verified not to escape
    """

    def __init__(self, config, capacity, transforms_checked):
        self.config = config
        self.capacity = capacity
        self.transforms_checked = transforms_checked

    def validate(self):
        if len(self.config) > self.capacity:
            return False
        for T in self.transforms_checked:
            if T(self.config) != self.config:
                return False
        return True

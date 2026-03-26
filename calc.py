import random

class Calculator:
    def __init__(self, seed=None):
        self.rng = random.Random(seed)

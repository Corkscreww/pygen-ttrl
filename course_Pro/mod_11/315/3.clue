class Random(_random.Random):

    VERSION = 3

    def __init__(self, x=None):

        self.seed(x)
        self.gauss_next = None
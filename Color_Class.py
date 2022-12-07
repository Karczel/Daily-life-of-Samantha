class Color
    def __init__(self, red, green, blue):
        self.r = red
        self.g = green
        self.b = blue

    @property
    def get_r(self):
        return self.r

    @property
    def get_g(self):
        return self.g

    @property
    def get_b(self):
        return self.b
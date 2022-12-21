class Color:
    def __init__(self, red=0, green=0, blue=0):
        self.__r = red
        self.__g = green
        self.__b = blue

    @property
    def r(self):
        return self.__r

    @property
    def g(self):
        return self.__g

    @property
    def b(self):
        return self.__b

    def __repr__(self):
        return f'{self.r} {self.g} {self.b}'
from Classes.Color_Class import Color
class Clothing:
    def __init__(self, type, name, r, g, b):
        self.__type = type
        self.__name = name
        self.__color = Color(int(r), int(g), int(b))

    @property
    def type(self):
        return self.__type
    @property
    def name(self):
        return self.__name
    @property
    def color(self):
        return self.__color

    def __repr__(self):
        return f'The {self.name} is a {self.type} piece, with this color: {self.color}'

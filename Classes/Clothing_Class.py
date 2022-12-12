from Classes.Color_Class import Color
class Clothing:
    def __init__(self,type,name,r,g,b):
        self.type = type
        self.name = name
        self.color = Color(int(r), int(g), int(b))

    @property
    def get_type(self):
        return self.type
    @property
    def get_name(self):
        return self.name
    @property
    def get_color(self):
        return self.color

    def __repr__(self):
        return f'The {self.name} is a {self.type} piece, with this color: {self.color}'

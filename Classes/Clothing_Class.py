import Color_Class
class Clothing:
    def __init__(self,type,name,r,g,b):
        self.type = type
        self.name = name
        self.color = Color(r,g,b)

    @property
    def get_name(self):
        return self.name
    @property
    def get_color(self):
        return self.color

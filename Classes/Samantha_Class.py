class Samantha:
    def __init__(self,name='Samantha',player_name='',hp=0,items=[], clothing=[],exercise=False,palette={}):
        self.name = name
        self.player = player_name
        self.hp = hp
        self.items = items
        self.clothing = clothing
        self.exercise = exercise
        self.palette = palette

    def add_items(self,item):
        self.append(items)
    def use_item(self, items):
        self.pop(items)

    def remove_clothing(self, clothing):
        self.pop(clothing)

    def wear_clothing(self, clothing):
        self.append(clothing)

    def change_clothing(self, clothing):
        if clothing_type(clothing) == "Jacket":
            if self.clothing in typeof clothing:
        elif clothing_type(clothing) == 'Shoes':
            if
        elif clothing_type(clothing) == 'Dress':
            if
        elif clothing_type(clothing) == 'Torso':
            if
        elif clothing_type(clothing) == "Lower half":
            if
        elif clothing_type(clothing) == "Socks":
            if

    @property
    def get_name(self):
        return self.name

    @property
    def get_playername(self):
        return self.palette

    @property
    def get_items(self):
        return self.hp

    @property
    def get_items(self):
        return self.items

    @property
    def get_clothing(self):
        return self.clothing

    @property
    def get_exercise(self):
        return self.exercise

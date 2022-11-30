class Samantha:
    def __init__(self,name='Samantha',player_name='',hp=0,items=[], clothing=[],closet=[],exercise=False,palette={}):
        self.name = name
        self.player = player_name
        self.hp = hp
        self.items = items
        self.clothing = Clothing()
        self.exercise = exercise
        self.closet = closet
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

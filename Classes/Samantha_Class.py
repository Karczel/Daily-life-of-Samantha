class Samantha:
    def __init__(self,name='Samantha',player_name='',hp=0,items=[], clothing={},exercise=False,palette={}):
        self.name = name
        self.player = player_name
        self.hp = hp
        self.items = items
        self.clothing = clothing
        self.exercise = exercise
        self.palette = palette

    def add_items(self,items):
        self.append(items)
    def use_item(self, items):
        self.remove(items)

    def remove_clothing(self, clothing):
        self.pop(clothing)

    def wear_clothing(self,clothing_type, clothing):
        self.update[clothing_type] = clothing

    def change_clothing(self, clothing_type,clothing):
        for k,v in self.clothing:
            if clothing_type == "Jacket":
                if k == clothing_type:
                    remove_clothing(self,k)
                    wear_clothing(self,clothing_type,clothing)
                else:
                    wear_clothing(clothing)
            elif clothing_type == 'Shoes':
                if k == clothing_type:
                    remove_clothing(self, k)
                    wear_clothing(self, clothing_type, clothing)
                else:
                    wear_clothing(clothing)
            elif clothing_type == 'Dress':
                if k == clothing_type or k == 'Torso' or k == 'Lower half':
                    remove_clothing(self, k)
                    wear_clothing(self, clothing_type, clothing)
                else:
                    wear_clothing(clothing)
            elif clothing_type == 'Torso':
                if k == clothing_type or k == 'Dress':
                    remove_clothing(self, k)
                    wear_clothing(self, clothing_type, clothing)
                else:
                    wear_clothing(clothing)
            elif clothing_type == "Lower half" or k == 'Dress':
                if k == clothing_type:
                    remove_clothing(self, k)
                    wear_clothing(self, clothing_type, clothing)
                else:
                    wear_clothing(clothing)
            elif clothing_type == "Socks":
                if k == clothing_type:
                    remove_clothing(self, k)
                    wear_clothing(self, clothing_type, clothing)
                else:
                    wear_clothing(clothing)

    @property
    def get_name(self):
        return self.name

    @property
    def get_playername(self):
        return self.palette

    @property
    def get_hp(self):
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

    @property
    def get_palette(self):
        return self.palette
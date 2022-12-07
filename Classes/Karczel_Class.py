class Karczel:
    def __init__(self, items=[], clothing={}, dinner=False, location='???', palette=[]):
        self.items = items
        self.clothing = clothing
        self.dinner = dinner
        self.location = location
        self.palette = palette

    def remove_clothing(self, clothing_type):
        self.clothing.pop(clothing_type)

    def wear_clothing(self, clothing_type, clothing):
        self.clothing.update[clothing_type] = clothing

    def change_clothing(self, clothing_type, clothing):
        for k, v in self.clothing:
            if clothing_type == "Jacket":
                if k == clothing_type:
                    self.remove_clothing(k)
                    self.wear_clothing(clothing_type, clothing)
                else:
                    self.wear_clothing(clothing_type, clothing)
            elif clothing_type == 'Shoes':
                if k == clothing_type:
                    self.remove_clothing(k)
                    self.wear_clothing(clothing_type, clothing)
                else:
                    self.wear_clothing(clothing_type, clothing)
            elif clothing_type == 'Dress':
                if k == clothing_type or k == 'Torso' or k == 'Lower half':
                    self.remove_clothing(k)
                    self.wear_clothing(clothing_type, clothing)
                else:
                    self.wear_clothing(clothing_type, clothing)
            elif clothing_type == 'Torso':
                if k == clothing_type or k == 'Dress':
                    self.remove_clothing(k)
                    self.wear_clothing(clothing_type, clothing)
                else:
                    self.wear_clothing(clothing_type, clothing)
            elif clothing_type == "Lower half" or k == 'Dress':
                if k == clothing_type:
                    self.remove_clothing(k)
                    self.wear_clothing(clothing_type, clothing)
                else:
                    self.wear_clothing(clothing_type, clothing)
            elif clothing_type == "Socks":
                if k == clothing_type:
                    self.remove_clothing(k)
                    self.wear_clothing(clothing_type, clothing)
                else:
                    self.wear_clothing(clothing_type, clothing)

    @property
    def get_items(self):
        return self.items

    @property
    def get_clothing(self):
        return self.clothing

    @property
    def get_dinner(self):
        return self.dinner

    @property
    def get_location(self):
        return self.location

    @property
    def get_palette(self):
        return self.palette



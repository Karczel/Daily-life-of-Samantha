class Karczel:
    def __init__(self,items=[],clothing={},dinner=False,location='???',palette={}):
        self.items = items
        self.closet = closet
        self.clothing = clothing
        self.dinner = dinner
        self.location = location
        self.palette = palette

        def remove_clothing(self, clothing):
            self.pop(clothing)

        def wear_clothing(self, clothing_type, clothing):
            self.update[clothing_type] = clothing

        def change_clothing(self, clothing_type, clothing):
            for k, v in self.clothing:
                if clothing_type == "Jacket":
                    if k == clothing_type:
                        remove_clothing(self, k)
                        wear_clothing(self, clothing_type, clothing)
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



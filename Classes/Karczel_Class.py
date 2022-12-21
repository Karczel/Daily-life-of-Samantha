class Karczel:
    def __init__(self, items=[],see=1, clothing={}, dinner=False, location='???',visited_locations=[], palette={}):
        self.__items = items
        self.__see = see
        self.__clothing = clothing
        self.__dinner = dinner
        self.__location = location
        self.__palette = palette
        self.__visited_locations = visited_locations

    def add_items(self, items):
        self.__items.append(items)
    def use_item(self, items):
        self.__items.remove(items)
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
    def items(self):
        return self.__items

    @property
    def see(self):
        return self.__see
    @see.setter
    def set_see(self, see):
        self.__see = see

    @property
    def clothing(self):
        return self.__clothing

    @property
    def dinner(self):
        return self.__dinner
    @dinner.setter
    def set_dinner(self, reply):
        if reply.lower() == 'yes':
            self.__dinner = True
        elif reply.lower() == 'no':
            self.__dinner = False

    @property
    def location(self):
        return self.__location

    @location.setter
    def set_location(self, location):
        self.__visited_locations.append(self.__location)
        self.__location = location

    @property
    def palette(self):
        return self.__palette



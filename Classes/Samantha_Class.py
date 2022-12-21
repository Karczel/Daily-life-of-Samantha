class Samantha:
    def __init__(self, name='Samantha', items=[], clothing={}, exercise=False, run=0, palette={}):
        self.__name = name
        self.__items = items
        self.__clothing = clothing
        self.__exercise = exercise
        self.__run = run
        self.__palette = palette

    def add_items(self, items):
        self.__items.append(items)
    def use_item(self, items):
        self.__items.remove(items)

    def remove_clothing(self, clothing_type):
        self.__clothing.pop(clothing_type)

    def wear_clothing(self, clothing_type, clothing):
        self.__clothing.update[clothing_type] = clothing

    def change_clothing(self, clothing_type, clothing):
        for k,v in self.clothing:
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
    def name(self):
        return self.__name

    @property
    def items(self):
        return self.__items

    @property
    def clothing(self):
        return self.__clothing

    @property
    def exercise(self):
        return self.__exercise
    @exercise.setter
    def set_exercise(self, exercise):
        self.__exercise = exercise

    @property
    def palette(self):
        return self.__palette
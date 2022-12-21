class Omisha:
    def __init__(self,items=[],location='???',palette={}):
        self.__items = items
        self.__location = location
        self.__palette = palette
    def add_items(self, items):
        self.__items.append(items)
    def use_item(self, items):
        self.__items.remove(items)
    @property
    def items(self):
        return self.__items
    @items.setter
    def set_items(self, items):
        self.__items = items

    @property
    def location(self):
        return self.__location

    @location.setter
    def set_location(self, location):
        return self.__location

    @property
    def palette(self):
        return self.__palette
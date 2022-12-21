class Zahur:
    def __init__(self,location='???',hungry=True,palette={}):
        self.__location = location
        self.__hungry = hungry
        self.__palette = palette

    def add_items(self, items):
        self.__items.append(items)
    def use_item(self, items):
        self.__items.remove(items)
    @property
    def items(self):
        return self.__items
    @property
    def location(self):
        return self.__location
    @location.setter
    def set_location(self,location):
        self.__location = location
    @property
    def hungry(self):
        return self.__hungry
    @hungry.setter
    def set_hungry(self,hungry):
        self.__hungry = hungry
    @property
    def palette(self):
        return self.__palette

    def __repr__(self):
        return f""
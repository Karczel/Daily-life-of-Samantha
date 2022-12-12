class Zahur:
    def __init__(self,location='???',hungry=True,palette={}):
        self.location = location
        self.hungry = hungry
        self.palette = palette

    @property
    def get_items(self):
        return self.items
    @property
    def get_location(self):
        return self.location
    @property
    def get_hungry(self):
        return self.hungry
    @property
    def get_palette(self):
        return self.palette

    def __repr__(self):
        return f""
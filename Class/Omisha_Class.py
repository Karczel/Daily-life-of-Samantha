class Omisha:
    def __init__(self,items=[],location='???',palette={}):
        self.items = items
        self.location = location
        self.palette = palette

        @property
        def get_items(self):
            return self.items
        @property
        def get_location(self):
            return self.location
        @property
        def get_palette(self):
            return self.palette
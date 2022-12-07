class Cat:
    def __init__(self,items=[],kittens={},palette={}):
        self.items = items
        self.kittens = kittens
        self.palette = palette
    #     item=[],kittens={color:amount}
    @property
    def get_items(self):
        return self.items
    @property
    def get_kittens(self):
        return self.kittens
    @property
    def get_palette(self):
        return self.palette
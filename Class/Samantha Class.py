class Samantha:
    def __init__(self,name='Samantha',player_name='',hp=0,items={}, buff={}, clothing=[],closet=[],exercise=False):
        self.name = name
        self.player = player_name
        self.hp = hp
        self.items = items
        self.buff = buff
        self.clothing = Clothing()
        self.exercise = exercise
        self.closet = closet

    def remove_buff(self):


    def add_buff(self):
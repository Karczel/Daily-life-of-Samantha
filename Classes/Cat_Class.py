class Cat:
    def __init__(self, name='???', general_desc='', color_text='', items=[], pronoun='???', kittens={}, palette={}):
        self.name = name
        self.desc = general_desc
        self.color  = color_text
        self.items = items
        self.pronoun = pronoun
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

    def __repr__(self):
        if self.kittens != {}:
            return f'{self.name}, a {self.color} cat with {self.desc}.'
        else:
            if len(self.kittens) == 1:
                return f'{self.name}, a {self.color} cat with {self.desc}. {self.pronoun} has {len(self.kittens)}, and it is {self.kittens[0]}'
            else:
                kitten_list = ''
                for i in self.kittens:
                    kitten_list += i + ', '
                return f'{self.name}, a {self.color} cat with {self.desc}. {self.pronoun} has {len(self.kittens)}, they are {kitten_list}'
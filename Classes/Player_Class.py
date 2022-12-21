class Player:
    def __init__(self, name, progress, date):
        self.__name = name
        self.__progress = progress
        self.__date = date

    @property
    def name(self):
        return self.__name

    @name.setter
    def set_name(self, name):
        self.__name = name

    @property
    def progress(self):
        return self.__progress

    @property
    def date(self):
        return self.__date

    def save(self, new_date, save_point):
        self.__date == new_date
        self.__progress.append(save_point)

    def __repr__(self):
        a = f'player: {self.name} last played: {self.date}'
        a += '\n progress:'
        for i in self.progress:
           a += f'{i} --> '
        a += 'present'
        return a

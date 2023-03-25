import datetime
class Player:
    def __init__(self, name, username, password, recover={}):
        self.__name = name
        self.__username = username
        self.__password = password
        self.__recover = recover
        self.__progress = {}
        # {'1':[progresses], '2':[], '3':[], '4':[]}
        self.__date = datetime.date.today()

    def save(self, new_date, save_point):
        self.__date == new_date
        self.__progress.append(save_point)

    def last_saved(self):
        if self.date.isoweekday() == 1:
            Day_of_week = 'Monday'
        elif self.date.isoweekday() == 2:
            Day_of_week = 'Tuesday'
        elif self.date.isoweekday() == 3:
            Day_of_week = 'Wednesday'
        elif self.date.isoweekday() == 4:
            Day_of_week = 'Thursday'
        elif self.date.isoweekday() == 5:
            Day_of_week = 'Friday'
        elif self.date.isoweekday() == 6:
            Day_of_week = 'Saturday'
        elif self.date.isoweekday() == 7:
            Day_of_week = 'Sunday'
        # when check on last played/save load should have this:
        print(f'Last played on {Day_of_week}, {self.date.day}/{self.date.month}/{self.date.year}')

    def continue_game(self):
        #

    def sign_up(self):
        #

    def log_in(self):
        #

    def recover_account(self):
        #


    @property
    def name(self):
        return self.__name

    @name.setter
    def set_name(self, name):
        self.__name = name

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @property
    def recover(self):
        return self.__recover

    @property
    def progress(self):
        return self.__progress

    @property
    def date(self):
        return self.__date

    def __repr__(self):
        a = f'player: {self.name} last played: {self.date}'
        a += '\n progress:'
        for i in self.progress:
           a += f'{i} --> '
        a += 'present'
        return a

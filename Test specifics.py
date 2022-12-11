Acheievements_list = open('Story_Output/Achievements.csv').read().splitlines()
d = [x.split(';') for x in Acheievements_list]
Acheievements = {i[0]:i[1] for i in d}
print(Acheievements)
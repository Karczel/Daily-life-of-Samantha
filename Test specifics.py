import copy
import sys,time
# Classes
from Classes.Color_Class import Color
from Classes.Omisha_Class import Omisha
from Classes.Zahur_Class import Zahur
from Classes.Karczel_Class import Karczel
from Classes.Samantha_Class import Samantha
from Classes.Clothing_Class import Clothing

Narrator_line_list = open("Story_Output/Narrator_line.csv", encoding="utf8").read().splitlines()
b = [x.split(';') for x in Narrator_line_list]
c = b[0]
Narrator_line = [{key: b[sub][idx] for idx, key in enumerate(c)}for sub in range(1,len(b))]
Question_line_list = open("Story_Output/Questions.csv", encoding="utf8").read().splitlines()
d = [x.split(';') for x in Question_line_list]
e = d[0]
Question_line = [{key: d[sub][idx] for idx, key in enumerate(e)}for sub in range(1,len(d))]
def open_character_line_files(filename):
    line_lists = open(filename, encoding="utf8").read().splitlines()
    line_split = [x.split(';') for x in line_lists]
    line = [{key: line_split[sub][idx] for idx, key in enumerate(line_split[0])} for sub in range(1, len(line_split))]
    return line

Samantha_line = open_character_line_files("Story_Output/Samantha_line.csv")
Karczel_line = open_character_line_files("Story_Output/Karczel_line.csv")
Omisha_line = open_character_line_files("Story_Output/Omisha_line.csv")
Zahur_line = open_character_line_files("Story_Output/Zahur_line.csv")

Acheievements_list = open('Story_Output/Achievements.csv', encoding="utf8").read().splitlines()
d = [x.split(';') for x in Acheievements_list]
Acheievements = {i[0]:i[1] for i in d}

def open_palette_files(filename):
    palette_list = open(filename, encoding="utf8").read().splitlines()
    palette_split = [x.split(',') for x in palette_list]
    return {i[0]: [Color(int(i[1]), int(i[2]), int(i[3]))] for i in palette_split}

S_palette = open_palette_files("Graphics/Palette/Samantha_palette.csv")
K_palette = open_palette_files("Graphics/Palette/Karczel_palette.csv")
O_palette = open_palette_files("Graphics/Palette/Omisha_palette.csv")
Z_palette = open_palette_files("Graphics/Palette/Zahur_palette.csv")

def open_clothing_files(filename):
    clothing_list = open(filename, encoding="utf8").read().splitlines()
    clothing_split1 = [x.split(',') for x in clothing_list]
    clothing_split2 = [{key: clothing_split1[sub][index] for index, key in enumerate(clothing_split1[0])} for sub in range(1,len(clothing_split1))]
    for i in clothing_split2:
        i["color"] = i["color"].split(' ')
    return clothing_split2

S_c = open_clothing_files('Clothing/Sam clothing.csv')
K_c = open_clothing_files('Clothing/Karczel clothing.csv')

def slowprint(s):
    temp_list = s.split('\\n')
    for i in temp_list:
        for lines in i + '\n':
            sys.stdout.write(lines)
            sys.stdout.flush()
            time.sleep(1. / 20)

def character_lines(character_name,s):
    f = copy.deepcopy(s)
    for i in f:
        for k, v in i.items():
            if k == 'Line':
                a = character_name + ': ' + v
                i.update({k: a})
    return f

Samantha_lines = character_lines('Samantha', Samantha_line)
Karczel_lines = character_lines('Karczel', Karczel_line)
Omisha_lines = character_lines('Omisha', Omisha_line)
Zahur_lines = character_lines('Zahur', Zahur_line)
table = []

# check variables
print(S_c)
print(S_palette)
print(Samantha_lines)
print(K_c)
print(K_palette)
print(Karczel_lines)
print(O_palette)
print(Omisha_lines)
print(Z_palette)
print(Zahur_lines)
print(Narrator_line)
print(Question_line)

# test functionality
print(Samantha_line[0]['Line'])
# slowprint(Question_line[0]['Question'])


player = input("Player name: ")

# Build characters
sam = Samantha('Samantha', player, [], {}, False, 0, S_palette)
karczel = Karczel([],1,{},False,'???',[],K_palette)
omisha = Omisha([],'???',O_palette)
zahur = Zahur('???', True, Z_palette)

# Build Closets
sam_closet = [Clothing(i['type'],i['clothing'],i['color'][0],i['color'][1],i['color'][2]) for i in S_c]
karczel_closet = [Clothing(i['type'],i['clothing'],i['color'][0],i['color'][1],i['color'][2]) for i in K_c]

for i in sam_closet:
    print(i)

# Build attributes
Karczel_items = []
for i in sam_closet:
    if 'Maid' in i.name:
        Karczel_items.append(i)

print(Karczel_items)

print('--- The End ---')
print('')
print('--- Nerd details ---')
print('')
print("Sam's closet")
for i in sam_closet:
    print(i)
print('')

print("Karczel's closet")
for i in karczel_closet:
    print(i)
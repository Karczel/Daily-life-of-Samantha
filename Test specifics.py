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


# ---code draft---
# previous choice  = []
# previous choice.append(choose)
# for i in previous choice
#     if i in choice_list
#     choice_list.pop(i)
# while choice_list != []
#     question loop
#     for i in range(set):
#         choice.append()
#         if "Karczel House":
#             a = str(i+1)
#     if "karczel house" or a:
#         break
#       if "Do nothing" or '1':
#         break
#
# festival = 1 -->loop?
# if festival == 1:
#     print(i['Fes T1'])
#
# if festival == 2:
#     print(i['Fes T2'])
#
# if festival == 3:
#     print(i['Fes T3'])

# ---properly---
choice = False
time_list = 0
previous_choice = []
choice_list = []
for i in Narrator_line:
    if i['Note'] == 'What you want to do':
        choice_list.append(i['Answer'])
while choice_list != []:
    while choice:
        choose = ''
        choice_number = []
        for i in Question_line:
            if i['Note'] == 'What you want to do':
                slowprint(i['Question'])
        for i in Narrator_line:
            if i['Note'] == 'What you want to do':
                choice_list.append(i['Answer'])
        for i in previous_choice:
            if i in choice_list:
                choice_list.pop(i)
        for i in enumerate(choice_list):
            slowprint(f'{i[0]+1} {i[1]}')
            if i[1] == "Kar H":
                karczel_choice = str(i[0]+1)
        choose = input()
        if choose in choice_list:
            break
    if choose == "Do nothing":
        break
    if choose == 'K House':
        break
    previous_choice.append(choose)
    # find number & str
    for j in enumerate(choice_list):
        if choose == j[1] or choose == str(j[0]+1):
            for i in Narrator_line:
                if i['Note'] == 'What you want to do':
                    if i['Answer'] == j[1]:
                        slowprint(i['Output'])

# festival early
if choose == 'Karczel House' or choose == karczel_choice:
    times = 1
    while choice_list != []:
        while choice:
            choose = ''
            choice_number = []
            for i in Question_line:
                if i['Note'] == 'Festival':
                    slowprint(i['Question'])
            for i in Narrator_line:
                if i['Note'] == 'Festival':
                    choice_list.append(i['Answer'])
            for i in Narrator_line:
                if time == 1:
                    if i['Note'] == 'Festival T1':
                        choice_list.append(i['Answer'])
                if time == 2:
                    if i['Note'] == 'Festival T2':
                        choice_list.append(i['Answer'])
                if time == 3:
                    if i['Note'] == 'Festival T3':
                        choice_list.append(i['Answer'])
            for i in previous_choice:
                if i in choice_list:
                    choice_list.pop(i)
            for i in enumerate(choice_list):
                slowprint(f'{i[0] + 1} {i[1]}')
                if i[1] == "Karczel House":
                    karczel_choice = str(i[0] + 1)
            choose = input()
            if choose in choice_list:
                break
        times += 1
        previous_choice.append(choose)



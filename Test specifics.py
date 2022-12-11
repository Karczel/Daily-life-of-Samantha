import sys,time
# Classes
from Classes.Color_Class import Color
from Classes.Omisha_Class import Omisha
from Classes.Zahur_Class import Zahur
from Classes.Karczel_Class import Karczel
from Classes.Samantha_Class import Samantha
from Classes.Clothing_Class import Clothing
from Classes.Cat_Class import Cat

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
    line = [{key: line_split[sub][idx-1] for idx, key in enumerate(line_split[0])} for sub in range(1, len(line_split))]
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
    for lines in s + '\n':
        sys.stdout.write(lines)
        sys.stdout.flush()
        time.sleep(2./10)
def character_lines(character_name,s):
    f = []
    for i in s:
        a = character_name + ': ' + i['Line']
        f.append(a)
    return f

Samantha_lines = character_lines('Samantha', Samantha_line)
Karczel_lines = character_lines('Karczel', Karczel_line)
Omisha_lines = character_lines('Omisha', Omisha_line)
Zahur_lines = character_lines('Zahur', Zahur_line)
table = [ ]

# check variables
print(Samantha_lines)
print(Karczel_lines)
print(Omisha_lines)
print(Zahur_lines)
print(Narrator_line)
print(Question_line)


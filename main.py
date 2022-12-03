import sys,time,csv
import Samantha_Class,Zahur_Class,Omisha_Class,Karczel_Class,Clothing_Class,Cat_Class,Person_Class,Person_Class

Narrator_line_list = open(filename).read().splitlines()
b = [x.split(';') for x in Narrator_line_list]
c = b[0]
Narrator_line = {key: [sub[idx] for sub in Narrator_line_list[1:]] for idx, key in enumerate(c)}
def open_character_line_files(filename):
    line_lists = open(filename).read().splitlines()
    line_split = [x.split(';') for x in line_lists]
    line = {texts[0]:[output for output in texts[1,len(texts-1)]] for texts in line_split}
    return line

Samantha_line = open_character_line_files("Samantha_line.csv")
Karczel_line = open_character_line_files("Karczel_line.csv")
Omisha_line = open_character_line_files("Omisha_line.csv")
Zahur_line = open_character_line_files("Zahur_line.csv")
Person1_line = open_character_line_files("Person1.csv")

def open_color_in_cloth(filename):
    color_lists = open(filename).read().splitlines()
    color_split = [x.split(" ") for x in color_lists]
    color = []
    for i in color_split:
        color.append(Color(i[0],i[1],i[2]))
    return color
def open_palette_files(filename):
    palette_list = open(filename).read().splitlines()
    for i in palette_list:
        i.split(',')
    return {i[0]: [Color(i[1], i[2], i[3])] for i in palette_list}

S_palette = open_palette_files("Samantha_palette.csv")
K_palette = open_palette_files("Karczel_palette.csv")
O_palette = open_palette_files("Omisha_palette.csv")
Z_palette = open_palette_files("Zahur_palette.csv")

def closet(**kwargs):
    for key, value in kwargs.
def open_clothing_files(filename):
    clothing_list = open(filename).read().splitlines()
    for i in clothing_list:
        i.split(',')
        for j in i[2]:
            j.split(' ')
    return {key: [sub[idx] in clothing_list] for idx, key in enumerate(clothing_list[0])}

S_c = open_clothing_files('Sam clothing.csv')
K_c = open_clothing_files('Karczel clothing.csv')

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2./10)
def slowprint_character(s,character):
    for c in s + '\n':
        sys.stdout.write(f'{character}: {c}')
        sys.stdout.flush()
        time.sleep(2./10)
def character_lines(character_name,s):
    f = []
    for i in s + '\n':
        a = character_name + ': ' + i
        f.append(a)
    return f

Samantha_lines = character_lines('Samantha',Samantha_line)
Karcze_lines = character_lines('Karczel',Karczel_line)
Omisha_lines = character_lines('Omisha',Omisha_line)
Zahur_lines = character_lines('Zahur',Zahur_line)
Person1_line = character_lines('Random person',Person1_line)
table = [ ]



# Build characters
sam = Samantha(,player,10000,,,S_palette)
karczel = Karczel()

# Build Closets
Closet =
sams_cloth = {Clothing(,S_clothing,) for i in }

# --- Start ---
slowprint(Narrator_line[0])
input = False
while input == False:
    real_input = input.lower()
    if real_input == a or real_input == b:
else:
    print(f"Please type in one of the choices given: \n"
          f"{a} \n"
          f"{b}")
if real_input == a:
    while
elif real_input == b:
    while


# --- End ---
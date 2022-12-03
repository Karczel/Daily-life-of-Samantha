import sys,time,csv
import Clothing,Graphics,Classes
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

def open_clothing_files(filename):
    clothing_list = open(filename).read().splitlines()
    for i in clothing_list:
        i.split(',')
        for j in i[2]:
            j.split(' ')
            # [[i[0],i[1],[r,g,b]]
    return {key: [sub[idx] in clothing_list] for idx, key in enumerate(clothing_list[0])}
# {1:i[1] 2:i[2] 3:[r,g,b]}
# get => for i,j in dict find name index > return same index from other category

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
sam_closet = [Clothing(i['type'],i['clothing'],i['color'][0],i['color'][1],i['color'][2]) for i in S_c]
karczel_closet = [Clothing(i['type'],i['clothing'],i['color'][0],i['color'][1],i['color'][2]) for i in K_c]

# --- Start ---
play = True
choice = False
while play != False:
    while choice:
        available_choices = []
        for i in Narrator_line:
            if i['Order'][0:2] == '00':
                available_choices.append({i['Choice Number'],i['Choice']})
                slowprint(Narrator_line[i]['Question'])
                print(f"Please type in one of the choices given: \n"
                  f"{available_choices[]} \n"
                  f"{available_choices[]}")
        choice = input()
        available_choices = []
        for i in Narrator_line:
            if i['Order'][0:3] == '000':
                available_choices.append(i['Choice'])
        if choice in []:
            if real_input == a:
                choice = True
    if choice == a:
        for i in Narrator_line:
            if i['Order'] == '0100000':
                slowprint(i['Result'])
        choice = False
        while choice:
    elif real_input == b:
        slowprint()

    # Replay?
    play_y_n = input('Do you still want to play?(Yes/No): ')
    while play_y_n.lower() != 'yes' or play_y_n.lower() != 'no':
        play_y_n = input('Do you still want to play?(Yes/No): ')
        if play_y_n.lower() == 'yes':
            play == True
        elif play == False:
            break
        else:
            print('Please input the right answer')

print("You've finished playing, have a nice day~")

# --- End ---
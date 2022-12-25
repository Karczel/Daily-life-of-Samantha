import copy
import sys
import time
# Classes
from Classes.Color_Class import Color
from Classes.Omisha_Class import Omisha
from Classes.Zahur_Class import Zahur
from Classes.Karczel_Class import Karczel
from Classes.Samantha_Class import Samantha
from Classes.Clothing_Class import Clothing
from Classes.Player_Class import Player

Narrator_line_list = open("Story_Output/Narrator_line.csv", encoding="utf8").read().splitlines()
b = [x.split(';') for x in Narrator_line_list]
c = b[0]
Narrator_line = [{key: b[sub][idx] for idx, key in enumerate(c)}for sub in range(1, len(b))]
Question_line_list = open("Story_Output/Questions.csv", encoding="utf8").read().splitlines()
d = [x.split(';') for x in Question_line_list]
e = d[0]
Question_line = [{key: d[sub][idx] for idx, key in enumerate(e)}for sub in range(1, len(d))]
Narrator_extra_line_list = open("Story_Output/Narrator_line_extra adjustments.csv", encoding="utf8").read().splitlines()
f = [x.split(';') for x in Narrator_extra_line_list]
g = f[0]
Narrator_extra_line = [{key: f[sub][idx] for idx, key in enumerate(g)}for sub in range(1, len(f))]

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
        for k, v in i.__items():
            if k == 'Line':
                a = character_name + ': ' + v
                i.update({k: a})
    return f

Samantha_lines = character_lines('Samantha', Samantha_line)
Karczel_lines = character_lines('Karczel', Karczel_line)
Omisha_lines = character_lines('Omisha', Omisha_line)
Zahur_lines = character_lines('Zahur', Zahur_line)
table = []

# players = earlier plays(up to 4 slots available)

# display earlier logs
player_list = {i[0]:i[1] for i in enumerate(players)}
if player_list != {}:
    for i in player_list:
        print(i)

# Get that player's achievements

# Delete player

# Clear all players

# recover account
for k, i in :
    choose question

# Build player
player_name = input("Player name: ")
player = Player(player_name)

# Build recovery question

# choose amount of question

# choose answer for each


# Build characters
sam = Samantha('Samantha', [], {}, False, 0, S_palette)
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

# --- Start ---
play = True
while play != False:
    choice = False
    previous_choice = []
    while choice:
        # wake up
        choice_list = []
        for i in Question_line:
            if i['Note'] == 'Wake up':
                slowprint(i['Question'])
        for i in Narrator_line:
            if i['Note'] == 'Wake up':
                choice_list.append(i['Answer'])
        for i in enumerate(choice_list):
            slowprint(f'{i[0] + 1} {i[1]}')
        choose = input("Enter your choice: ")
        for i in range(len(choice_list)):
            if choose == choice_list[i] or choose == str(i+1):
                break
        print('Wrong answer')

    # The end
    exec('end_graphic')
    # acheivements
    count = 0
    if sam.exercise == True:
        slowprint(Acheievements['Run 1 time'])
        count += 1
        if sam.__run == 2:
            slowprint(Acheievements['Run 2 times'])
    else:
        slowprint(Acheievements["Didn't Run today"])

    # about karczel
    if karczel.location != '???':
        if '___Festival' in karczel.__visited_locations:
            count += 1
            slowprint(Acheievements['Go to the Festival'])
            if karczel.see == 1:
                slowprint(Acheievements['See the 1st Tournament'])
            elif karczel.see == 2:
                slowprint(Acheievements['See the 2nd Tournament'])
            elif karczel.see == 3:
                slowprint(Acheievements['See the 3rd Tournament'])
        if karczel.dinner != False:
            if "Fancy restaurant" in karczel.__visited_locations:
                slowprint(Acheievements["Eat dinner at the fancy place"])
            else:
                if "Omelette and rice" in sam.items:
                    slowprint(Acheievements["Eat dinner at Karczel's place"])
                elif "Sam's food" in sam.items:
                    slowprint(Acheievements["Make dinner for Karczel"])
        else:
            slowprint(Acheievements["Eat dinner at home"])
    else:
        slowprint(Acheievements["Didn't see Karczel"])

    # about zahur
    if zahur.location != '???':
        count += 1
        if 'buttered toast' in sam.items:
            slowprint(Acheievements['Sam still carry toast'])
        elif 'buttered toast' in table:
            slowprint(Acheievements['Forgotten the Toast at the table'])
        elif zahur.hungry == False:
            slowprint(Acheievements['Gave Zahur toast'])
    else:
        slowprint(Acheievements["Didn't see Zahur"])

    # about omisha
    if omisha.location != '???':
        count += 1
        slowprint(Acheievements['See Omisha'])
        if 'art supplies' in omisha.items:
            slowprint(Acheievements['Buy Omisha Art supplies'])
        else:
            slowprint(Acheievements['Rescue kittens'])
            if 'cat' in sam.items:
                slowprint(Acheievements['Adopt kittens'])
    else:
        slowprint(Acheievements["Didn't see Omisha"])

    # lazy day?
    if count == 0:
        slowprint(Acheievements['Did nothing today'])

    slowprint("That everything that happened today")

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

# --- The End ---
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
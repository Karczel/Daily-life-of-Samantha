import sys,time
# Classes
from Classes.Color_Class import Color
from Classes.Omisha_Class import Omisha
from Classes.Zahur_Class import Zahur
from Classes.Karczel_Class import Karczel
from Classes.Samantha_Class import Samantha
from Classes.Clothing_Class import Clothing
from Classes.Cat_Class import Cat
# Graphics
from Graphics import end_graphic

# # Pictures
# # The end
# exec('end_graphic')


Narrator_line_list = open("Story_Output/Narrator_line.csv").read().splitlines()
b = [x.split(';') for x in Narrator_line_list]
c = b[0]
Narrator_line = [{key: b[sub][idx] for idx, key in enumerate(c)}for sub in range(1,len(b))]
def open_character_line_files(filename):
    line_lists = open(filename).read().splitlines()
    line_split = [x.split(';') for x in line_lists]
    line = [{key: line_split[sub][idx] for idx, key in enumerate(line_split[0])} for sub in range(1, len(line_split))]
    return line

Samantha_line = open_character_line_files("Story_Output/Samantha_line.csv")
Karczel_line = open_character_line_files("Story_Output/Karczel_line.csv")
Omisha_line = open_character_line_files("Story_Output/Omisha_line.csv")
Zahur_line = open_character_line_files("Story_Output/Zahur_line.csv")
Person1_line = open_character_line_files("Story_Output/Person1.csv")

Acheievements_list = open('Story_Output/Achievements.csv').read().splitlines()
d = [x.split(',') for x in Acheievements_list]
Acheievements = {i[0]:i[1] for i in d}

def open_palette_files(filename):
    palette_list = open(filename).read().splitlines()
    palette_split = [x.split(',') for x in palette_list]
    return {i[0]: [Color(int(i[1]), int(i[2]), int(i[3]))] for i in palette_split}

S_palette = open_palette_files("Graphics/Palette/Samantha_palette.csv")
K_palette = open_palette_files("Graphics/Palette/Karczel_palette.csv")
O_palette = open_palette_files("Graphics/Palette/Omisha_palette.csv")
Z_palette = open_palette_files("Graphics/Palette/Zahur_palette.csv")

def open_clothing_files(filename):
    clothing_list = open(filename).read().splitlines()
    clothing_split1 = [x.split(',') for x in clothing_list]
    clothing_split2 = [{key: clothing_split1[sub][index] for index, key in enumerate(clothing_split1[0])} for sub in range(1,len(clothing_split1))]
    for i in clothing_split2:
        i['color'] = i['color'].split(' ')
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
    for i in s + '\n':
        a = character_name + ': ' + i
        f.append(a)
    return f

Samantha_lines = character_lines('Samantha',Samantha_line)
Karczel_lines = character_lines('Karczel', Karczel_line)
Omisha_lines = character_lines('Omisha',Omisha_line)
Zahur_lines = character_lines('Zahur',Zahur_line)
Person1_line = character_lines('Random person',Person1_line)
table = [ ]


player = input("Player name: ")
# Build attributes
Karczel_items = []
for i in S_c:
    if 'Maid' in i['clothing']:
        Karczel_items.append(i)

# Build characters
sam = Samantha('Samantha',player,10000,[],{},False,S_palette)
karczel = Karczel('Karczel')
omisha = Omisha('Omisha')
zahur = Zahur('Zahur')
cat1 =  Cat('')
cat2 = Cat('')

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
            # 000000 question
            if i['Order'][0:2] == '00':
                question = i['Question']
                available_choices.append({i['Choice Number'],i['Choice']})
        slowprint(question+'\n')
        slowprint("Please type in one of the choices given: \n")
        for k,v in available_choices:
            print(f"{k}:{v} \n")
        choice = input()
        if choice in list(available_choices.values().lower()) or choice in list(available_choices.keys()):
            choice = True
        else:
            print('Wrong answer')
    if choice == available_choices['1'].lower() or choice == '1':
        for i in Narrator_line:
            # 000 choice 1
            if i['Order'][0:2] == '00' and i['Choice Number'] == '1':
                slowprint(i['Result'])
        choice = False
        while choice:
            available_choices = []
            for i in Narrator_line:
                # 010 question
                if i['Order'][0:3] == '010':
                    question = i['Question']
            available_choices.append({i['Choice Number'], i['Choice']})
            slowprint(question+'\n')
            print(f"Please type in one of the choices given: \n")
            for k, v in available_choices:
                print(f"{k}:{v} \n")
            choice = input()
            if choice in list(available_choices.values().lower()) or choice in list(available_choices.keys()):
                choice = True
            else:
                print('Wrong answer')
        if choice == available_choices['1'].lower() or choice == '1':
            for i in Narrator_line:
                # 010 choice 1
                if i['Order'][0:2] == '00' and i['Choice Number'] == '1':
                    slowprint(i['Result'])
            choice = False
            while choice:
                available_choices = []
                for i in Narrator_line:
                    # 0110 question
                    if i['Order'][0:3] == '010':
                        question = i['Question']
                available_choices.append({i['Choice Number'], i['Choice']})
                slowprint(question+'\n')
                print(f"Please type in one of the choices given: \n")
                for k, v in available_choices:
                    print(f"{k}:{v} \n")
                choice = input()
                if choice in list(available_choices.values().lower()) or choice in list(available_choices.keys()):
                    choice = True
                else:
                    print('Wrong answer')
            if choice == available_choices['1'].lower() or choice == '1':
                for i in Narrator_line:
                    # 0110 choice 1
                    if i['Order'][0:2] == '00' and i['Choice Number'] == '1':
                        slowprint(i['Result'])
                choice = False
                while choice:
                    available_choices = []
                    for i in Narrator_line:
                        # 01110 question
                        if i['Order'][0:3] == '010':
                            question = i['Question']
                    available_choices.append({i['Choice Number'], i['Choice']})
                    slowprint(question+'\n')
                    print(f"Please type in one of the choices given: \n")
                    for k, v in available_choices:
                        print(f"{k}:{v} \n")
                    choice = input()
                    if choice in list(available_choices.values().lower()) or choice in list(available_choices.keys()):
                        choice = True
                    else:
                        print('Wrong answer')
                if choice == available_choices['1'].lower() or choice == '1':
                    for i in Narrator_line:
                        # 01110 choice 1
                        if i['Order'][0:2] == '00' and i['Choice Number'] == '1':
                            slowprint(i['Result'])
                    choice = False
                    while choice:
                        available_choices = []
                        for i in Narrator_line:
                            # 011110 question
                            if i['Order'][0:3] == '010':
                                question = i['Question']
                        available_choices.append({i['Choice Number'], i['Choice']})
                        slowprint(question+'\n')
                        print(f"Please type in one of the choices given: \n")
                        for k, v in available_choices:
                            print(f"{k}:{v} \n")
                        choice = input()
                        if choice in list(available_choices.values().lower()) or choice in list(
                                available_choices.keys()):
                            choice = True
                        else:
                            print('Wrong answer')
                    if choice == available_choices['1'].lower() or choice == '1':
                        for i in Narrator_line:
                            # 011110 choice 1
                            if i['Order'][0:2] == '00' and i['Choice Number'] == '1':
                                slowprint(i['Result'])
                        choice = False
                        while choice:
                            available_choices = []
                            for i in Narrator_line:
                                # 0111110 question
                                if i['Order'][0:3] == '010':
                                    question = i['Question']
                            available_choices.append({i['Choice Number'], i['Choice']})
                            slowprint(question+'\n')
                            print(f"Please type in one of the choices given: \n")
                            for k, v in available_choices:
                                print(f"{k}:{v} \n")
                            choice = input()
                            if choice in list(available_choices.values().lower()) or choice in list(
                                    available_choices.keys()):
                                choice = True
                            else:
                                print('Wrong answer')
                        if choice == available_choices['1'].lower() or choice == '1':
                            for i in Narrator_line:
                                # 0111110 choice 1
                                if i['Order'][0:2] == '00' and i['Choice Number'] == '1':
                                    slowprint(i['Result'])
                            choice = False
                            while choice:
                                available_choices = []
                                for i in Narrator_line:
                                    # 01111110 question
                                    if i['Order'][0:3] == '010':
                                        question = i['Question']
                                available_choices.append({i['Choice Number'], i['Choice']})
                                slowprint(question+'\n')
                                print(f"Please type in one of the choices given: \n")
                                for k, v in available_choices:
                                    print(f"{k}:{v} \n")
                                choice = input()
                                if choice in list(available_choices.values().lower()) or choice in list(
                                        available_choices.keys()):
                                    choice = True
                                else:
                                    print('Wrong answer')

            if choice == available_choices['2'].lower() or choice == '2':

    elif choice == available_choices['2'].lower() or choice == '2':
        for i in Narrator_line:
            # 000 choice 2
            if i['Order'][0:2] == '00' and i['Choice Number'] == '2':
                slowprint(i['Result'])
        choice = False
        while choice:
            for i in Narrator_line:
                # 020 question
                if i['Order'][0:3] == '010':
                    question = i['Question']
                    available_choices.append({i['Choice Number'], i['Choice']})
            slowprint(question)
            print(f"Please type in one of the choices given: \n")
            for k, v in available_choices:
                print(f"{k}:{v} \n")
                choice = input()
                if choice in list(available_choices.values()):
                    choice = True
                else:
                    print('Wrong answer')
        if choice == available_choices[]:
            slowprint()

    # The end
    exec('end_graphic')
    # acheivements
    count = 0
    if sam.exercise == True:
        slowprint(Acheievements['Run 1 time'])
        count += 1
        if sam.run == 2:
            slowprint(Acheievements['Run 2 times'])
    else:
        slowprint(Acheievements["Didn't Run today"])

    # about karczel
    if karczel.location != '???':
        if '___Festival' in karczel.visited_locations:
            count += 1
            slowprint(Acheievements['Go to the Festival'])
            if karczel.see == 1:
                slowprint(Acheievements['See the 1st Tournament'])
            elif karczel.see == 2:
                slowprint(Acheievements['See the 2nd Tournament'])
            elif karczel.see == 3:
                slowprint(Acheievements['See the 3rd Tournament'])
        if karczel.dinner != False:
            if "Fancy restaurant" in karczel.visited_locations:
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
        elif cat1.location != '???':
            slowprint(Acheievements['Rescue kittens'])
            if cat1 and cat2 in sam.items:
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

# --- End ---
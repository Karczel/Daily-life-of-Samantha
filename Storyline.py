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

# check variables
# print(Samantha_line)
# print(Karczel_line)
# print(Zahur_line)
# print(Omisha_line)
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
# print(S_c)
# print(S_palette)
# print(Samantha_lines)
# print(K_c)
# print(K_palette)
# print(Karczel_lines)
# print(O_palette)
# print(Omisha_lines)
# print(Z_palette)
# print(Zahur_lines)
# print(Narrator_line)
# print(Question_line)

# test functionality
# print(Samantha_line[0]['Line'])


player = input("Player name: ")
# Build attributes
Karczel_items = []
for i in S_c:
    if 'Maid' in i['clothing']:
        Karczel_items.append(i)

# Build characters
sam = Samantha('Samantha', player, [], {}, False, 0, S_palette)
karczel = Karczel('Karczel')
omisha = Omisha('Omisha')
zahur = Zahur('???',True,Z_palette)

# Build Closets
sam_closet = [Clothing(i['type'],i['clothing'],i['color'][0],i['color'][1],i['color'][2]) for i in S_c]
karczel_closet = [Clothing(i['type'],i['clothing'],i['color'][0],i['color'][1],i['color'][2]) for i in K_c]

# --- Start ---
play = True
while play != False:
    choice = False
    while choice:
        # wake up
        choice_list = []
        for i in Question_line:
            if i['Note'] == 'Wake up':
                slowprint(i['Question'])
        for i in Narrator_line:
            if i['Note'] == 'Wake up':
                choice_list.append(i['Answer'])
        for i in range(len(choice_list)):
            print(f"{i}: {choice_list[i]}")
        choose = input("Enter your choice: ")
        for i in range(len(choice_list)):
            if choose == choice_list[i] or choose == str(i+1):
                break
        print('Wrong answer')

    if choose.lower() == 'yes' or choose == '1':
        # yes
        for i in Narrator_line:
            if i['Note'] == 'Wake up':
                if i['Answer'] == 'Yes':
                    slowprint(i['Output'])
        while choice:
            # wake up
            choice_list = []
            for i in Question_line:
                if i['Note'] == 'Wake up':
                    slowprint(i['Question'])
            for i in Narrator_line:
                if i['Note'] == 'Wake up':
                    choice_list.append(i['Answer'])
            for i in range(len(choice_list)):
                print(f"{i}: {choice_list[i]}")
            choose = input("Enter your choice: ")
            for i in range(len(choice_list)):
                if choose == choice_list[i] or choose == str(i + 1):
                    break
            print('Wrong answer')

    if choose.lower() == 'no' or choose == '2':
        #no
        for i in Narrator_line:
            if i['Note'] == 'Wake up':
                if i['Answer'] == 'No':
                    slowprint(i['Output'])
        while choice:
            # sure?
            choice_list = []
            for i in Question_line:
                if i['Note'] == 'Sure?':
                    slowprint(i['Question'])
            for i in Narrator_line:
                if i['Note'] == 'Sure?':
                    choice_list.append(i['Answer'])
            for i in range(len(choice_list)):
                print(f"{i}: {choice_list[i]}")
            choose = input("Enter your choice: ")
            for i in range(len(choice_list)):
                if choose == choice_list[i] or choose == str(i + 1):
                    break
            print('Wrong answer')
        if choose == 'yes' or choose == '2':
            # yes
            for i in Narrator_line:
                if i['Note'] == 'Sure?':
                    if i['Answer'] == 'Yes':
                        slowprint(i['Output'])
            while choice:
                # where go next?
                choice_list = []
                for i in Question_line:
                    if i['Note'] == 'What you want to do':
                        slowprint(i['Question'])
                for i in Narrator_line:
                    if i['Note'] == 'What you want to do':
                        choice_list.append(i['Answer'])
                for i in range(len(choice_list)):
                    print(f"{i}: {choice_list[i]}")
                choose = input("Enter your choice: ")
                for i in range(len(choice_list)):
                    if choose == choice_list[i] or choose == str(i + 1):
                        break
                print('Wrong answer')

            if choose.lower() == "Omisha's room" or choose == '5':
                # Omisha's room
                for i in Narrator_line:
                    if i['Note'] == 'What you want to do':
                        if i['Answer'] == "Omisha's room":
                            slowprint(i['Output'])

            elif choose.lower() == "karczel's house" or choose == '4':
                # the kitchen
                for i in Narrator_line:
                    if i['Note'] == 'What you want to do':
                        if i['Answer'] == "Karczel's House":
                            slowprint(i['Output'])

            elif choose.lower() == 'The kitchen' or choose == '3':
                # the kitchen
                for i in Narrator_line:
                    if i['Note'] == 'What you want to do':
                        if i['Answer'] == 'The kitchen':
                            slowprint(i['Output'])

            elif choose.lower() == 'zahur’s room' or choose == '2':
                # Zahur’s room
                for i in Narrator_line:
                    if i['Note'] == 'What you want to do':
                        if i['Answer'] == 'Zahur’s room':
                            slowprint(i['Output'])

            # choose.lower() == 'do nothing' or choose == '1':
            # Do nothing(void)
        if choose == "I've changed my mind" or choose == '1':
            # changed(void)
            while choice:
                # 1 run
                choice_list = []
                for i in Question_line:
                    if i['Note'] == 'Finish 1 run':
                        slowprint(i['Question'])
                for i in Narrator_line:
                    if i['Note'] == 'Finish 1 run':
                        choice_list.append(i['Answer'])
                for i in range(len(choice_list)):
                    print(f"{i}: {choice_list[i]}")
                choose = input("Enter your choice: ")
                for i in range(len(choice_list)):
                    if choose == choice_list[i] or choose == str(i + 1):
                        break
                print('Wrong answer')
            if choose.lower() == "zahur’s room" or choose == '4':
                # zahur room
                for i in Narrator_line:
                    if i['Note'] == 'Finish 1 run':
                        if i['Answer'] == "Zahur’s room":
                            slowprint(i['Output'])
                while choice:
                    # what do
                    choice_list = []
                    for i in Question_line:
                        if i['Note'] == 'What you want to do':
                            slowprint(i['Question'])
                    for i in Narrator_line:
                        if i['Note'] == 'What you want to do':
                            choice_list.append(i['Answer'])
                    choice_list.pop("Zahur’s room")
                    for i in range(len(choice_list)):
                        print(f"{i}: {choice_list[i]}")
                    choose = input("Enter your choice: ")
                    for i in range(len(choice_list)):
                        if choose == choice_list[i] or choose == str(i + 1):
                            break
                    print('Wrong answer')
                if choose.lower() == "The kitchen" or choose == '2':
                    # The kitchen
                    for i in Narrator_line:
                        if i['Note'] == 'What you want to do':
                            if i['Answer'] == "The kitchen":
                                slowprint(i['Output'])
                    while choice:
                        # what do
                        choice_list = []
                        for i in Question_line:
                            if i['Note'] == 'What you want to do':
                                slowprint(i['Question'])
                        for i in Narrator_line:
                            if i['Note'] == 'What you want to do':
                                choice_list.append(i['Answer'])
                        choice_list.pop("Zahur’s room")
                        choice_list.pop("The kitchen")
                        for i in range(len(choice_list)):
                            print(f"{i}: {choice_list[i]}")
                        choose = input("Enter your choice: ")
                        for i in range(len(choice_list)):
                            if choose == choice_list[i] or choose == str(i + 1):
                                break
                        print('Wrong answer')
                    if choose.lower() == "Karczel's House" or choose == '2':
                        # The kitchen
                        for i in Narrator_line:
                            if i['Note'] == 'What you want to do':
                                if i['Answer'] == "The kitchen":
                                    slowprint(i['Output'])
                        while choice:
                            # what do
                            choice_list = []
                            for i in Question_line:
                                if i['Note'] == 'What you want to do':
                                    slowprint(i['Question'])
                            for i in Narrator_line:
                                if i['Note'] == 'What you want to do':
                                    choice_list.append(i['Answer'])
                            choice_list.pop("Zahur’s room")
                            choice_list.pop("The kitchen")
                            choice_list.pop("Karczel's House")
                            for i in range(len(choice_list)):
                                print(f"{i}: {choice_list[i]}")
                            choose = input("Enter your choice: ")
                            for i in range(len(choice_list)):
                                if choose == choice_list[i] or choose == str(i + 1):
                                    break
                            print('Wrong answer')
                    if choose.lower() == "Omisha's room" or choose == '2':
                        # The kitchen
                        for i in Narrator_line:
                            if i['Note'] == 'What you want to do':
                                if i['Answer'] == "The kitchen":
                                    slowprint(i['Output'])

            elif choose.lower() == "omisha’s room" or choose == '3':
                # omisha's room
                for i in Narrator_line:
                    if i['Note'] == 'Finish 1 run':
                        if i['Answer'] == "Omisha’s room":
                            slowprint(i['Output'])

            elif choose.lower() == 'the kitchen' or choose == '2':
                # the kitchen
                for i in Narrator_line:
                    if i['Note'] == 'Finish 1 run':
                        if i['Answer'] == 'The kitchen':
                            slowprint(i['Output'])

            elif choose.lower() == 'another run' or choice == '1':
                # another run
                for i in Narrator_line:
                    if i['Note'] == 'Finish 1 run':
                        if i['Answer'] == 'Another run':
                            slowprint(i['Output'])
                while choice:
                    # See Karczel?
                    choice_list = []
                    for i in Question_line:
                        if i['Note'] == 'See Karczel?':
                            slowprint(i['Question'])
                    for i in Narrator_line:
                        if i['Note'] == 'See Karczel?':
                            choice_list.append(i['Answer'])
                    for i in range(len(choice_list)):
                        print(f"{i}: {choice_list[i]}")
                    choose = input("Enter your choice: ")
                    for i in range(len(choice_list)):
                        if choose == choice_list[i] or choose == str(i + 1):
                            break
                    print('Wrong answer')
                if choose.lower() == 'no' or choose == '2':
                    # no
                    for i in Narrator_line:
                        if i['Note'] == 'See Karczel?':
                            if i['Answer'] == 'No':
                                slowprint(i['Output'])
                    while choice:
                        # what do next?
                        choice_list = []
                        for i in Question_line:
                            if i['Note'] == 'What you want to do':
                                slowprint(i['Question'])
                        for i in Narrator_line:
                            if i['Note'] == 'What you want to do':
                                choice_list.append(i['Answer'])
                        choice_list.pop("Karczel's House")
                        for i in range(len(choice_list)):
                            print(f"{i}: {choice_list[i]}")
                        choose = input("Enter your choice: ")
                        for i in range(len(choice_list)):
                            if choose == choice_list[i] or choose == str(i + 1):
                                break
                        print('Wrong answer')
                    if choose.lower() == "omisha's room" or choose == '3':
                        # omisha
                        for i in Narrator_line:
                            if i['Note'] == 'What you want to do':
                                if i['Answer'] == "Omisha's room":
                                    slowprint(i['Output'])
                        while choice:
                            # what do next?
                            choice_list = []
                            for i in Question_line:
                                if i['Note'] == 'What you want to do':
                                    slowprint(i['Question'])
                            for i in Narrator_line:
                                if i['Note'] == 'What you want to do':
                                    choice_list.append(i['Answer'])
                            choice_list.pop("Karczel's House")
                            choice_list.pop("Omisha's room")
                            for i in range(len(choice_list)):
                                print(f"{i}: {choice_list[i]}")
                            choose = input("Enter your choice: ")
                            for i in range(len(choice_list)):
                                if choose == choice_list[i] or choose == str(i + 1):
                                    break
                            print('Wrong answer')
                        if choose.lower() == "The kitchen" or choose == '2':
                            # kitchen
                            for i in Narrator_line:
                                if i['Note'] == 'What you want to do':
                                    if i['Answer'] == "The kitchen":
                                        slowprint(i['Output'])
                            while choice:
                                # what do next?
                                choice_list = []
                                for i in Question_line:
                                    if i['Note'] == 'What you want to do':
                                        slowprint(i['Question'])
                                for i in Narrator_line:
                                    if i['Note'] == 'What you want to do':
                                        choice_list.append(i['Answer'])
                                choice_list.pop("Karczel's House")
                                choice_list.pop("Omisha's room")
                                choice_list.pop("The kitchen")
                                for i in range(len(choice_list)):
                                    print(f"{i}: {choice_list[i]}")
                                choose = input("Enter your choice: ")
                                for i in range(len(choice_list)):
                                    if choose == choice_list[i] or choose == str(i + 1):
                                        break
                                print('Wrong answer')
                            if choose.lower() == "zahur’s room;" or choose == '1':
                                # see zahur
                                for i in Narrator_line:
                                    if i['Note'] == 'What you want to do':
                                        if i['Answer'] == "Zahur’s room;":
                                            slowprint(i['Output'])
                            slowprint("There's nothing else to do today.")
                        elif choose.lower() == "zahur’s room" or choose == '1':
                            # see zahur
                            for i in Narrator_line:
                                if i['Note'] == 'What you want to do':
                                    if i['Answer'] == "Zahur’s room":
                                        slowprint(i['Output'])
                            while choice:
                                # what do next?
                                choice_list = []
                                for i in Question_line:
                                    if i['Note'] == 'What you want to do':
                                        slowprint(i['Question'])
                                for i in Narrator_line:
                                    if i['Note'] == 'What you want to do':
                                        choice_list.append(i['Answer'])
                                choice_list.pop("Karczel's House")
                                choice_list.pop("Omisha's room")
                                choice_list.pop("Zahur’s room")
                                for i in range(len(choice_list)):
                                    print(f"{i}: {choice_list[i]}")
                                choose = input("Enter your choice: ")
                                for i in range(len(choice_list)):
                                    if choose == choice_list[i] or choose == str(i + 1):
                                        break
                                print('Wrong answer')
                            if choose.lower() == "the kitchen" or choose == '1':
                                # kitchen
                                for i in Narrator_line:
                                    if i['Note'] == 'What you want to do':
                                        if i['Answer'] == "The kitchen":
                                            slowprint(i['Output'])
                            slowprint("There's nothing else to do today.")
                    elif choose.lower() == 'the kitchen' or choose == '2':
                        # kitchen
                        for i in Narrator_line:
                            if i['Note'] == 'What you want to do':
                                if i['Answer'] == 'The kitchen':
                                    slowprint(i['Output'])
                        while choice:
                            # what do next?
                            choice_list = []
                            for i in Question_line:
                                if i['Note'] == 'What you want to do':
                                    slowprint(i['Question'])
                            for i in Narrator_line:
                                if i['Note'] == 'What you want to do':
                                    choice_list.append(i['Answer'])
                            choice_list.pop("Karczel's House")
                            choice_list.pop('The kitchen')
                            for i in range(len(choice_list)):
                                print(f"{i}: {choice_list[i]}")
                            choose = input("Enter your choice: ")
                            for i in range(len(choice_list)):
                                if choose == choice_list[i] or choose == str(i + 1):
                                    break
                            print('Wrong answer')
                        if choose.lower() == "omisha's room" or choose == '2':
                            # omisha room
                            for i in Narrator_line:
                                if i['Note'] == 'What you want to do':
                                    if i['Answer'] == "Omisha's room":
                                        slowprint(i['Output'])
                            while choice:
                                # what do next?
                                choice_list = []
                                for i in Question_line:
                                    if i['Note'] == 'What you want to do':
                                        slowprint(i['Question'])
                                for i in Narrator_line:
                                    if i['Note'] == 'What you want to do':
                                        choice_list.append(i['Answer'])
                                choice_list.pop("Karczel's House")
                                choice_list.pop("The kitchen")
                                choice_list.pop("Omisha's room")
                                for i in range(len(choice_list)):
                                    print(f"{i}: {choice_list[i]}")
                                choose = input("Enter your choice: ")
                                for i in range(len(choice_list)):
                                    if choose == choice_list[i] or choose == str(i + 1):
                                        break
                                print('Wrong answer')
                            if choose.lower() == "zahur’s room;" or choose == '1':
                                # see zahur
                                for i in Narrator_line:
                                    if i['Note'] == 'What you want to do':
                                        if i['Answer'] == "Zahur’s room;":
                                            slowprint(i['Output'])
                            slowprint("There's nothing else to do today.")
                        elif choose.lower() == "zahur’s room" or choose == '1':
                            # see zahur
                            for i in Narrator_line:
                                if i['Note'] == 'What you want to do':
                                    if i['Answer'] == "Zahur’s room":
                                        slowprint(i['Output'])
                            while choice:
                                # what do next?
                                choice_list = []
                                for i in Question_line:
                                    if i['Note'] == 'What you want to do':
                                        slowprint(i['Question'])
                                for i in Narrator_line:
                                    if i['Note'] == 'What you want to do':
                                        choice_list.append(i['Answer'])
                                choice_list.pop("Karczel's House")
                                choice_list.pop("The kitchen")
                                choice_list.pop("Zahur’s room")
                                for i in range(len(choice_list)):
                                    print(f"{i}: {choice_list[i]}")
                                choose = input("Enter your choice: ")
                                for i in range(len(choice_list)):
                                    if choose == choice_list[i] or choose == str(i + 1):
                                        break
                                print('Wrong answer')
                            if choose.lower() == "omisha's room" or choose == '1':
                                # omisha
                                for i in Narrator_line:
                                    if i['Note'] == 'What you want to do':
                                        if i['Answer'] == "Omisha's room":
                                            slowprint(i['Output'])
                            slowprint("There's nothing else to do today.")
                    elif choose.lower() == "zahur’s room" or choose == '1':
                        # zahur room
                        for i in Narrator_line:
                            if i['Note'] == 'What you want to do':
                                if i['Answer'] == "Zahur’s room":
                                    slowprint(i['Output'])
                        while choice:
                            # what do next?
                            choice_list = []
                            for i in Question_line:
                                if i['Note'] == 'What you want to do':
                                    slowprint(i['Question'])
                            for i in Narrator_line:
                                if i['Note'] == 'What you want to do':
                                    choice_list.append(i['Answer'])
                            choice_list.pop("Karczel's House")
                            choice_list.pop("Zahur’s room")
                            for i in range(len(choice_list)):
                                print(f"{i}: {choice_list[i]}")
                            choose = input("Enter your choice: ")
                            for i in range(len(choice_list)):
                                if choose == choice_list[i] or choose == str(i + 1):
                                    break
                            print('Wrong answer')
                        if choose.lower() == "omisha's room" or choose == '2':
                            # omisha room
                            for i in Narrator_line:
                                if i['Note'] == 'What you want to do':
                                    if i['Answer'] == "Omisha's room":
                                        slowprint(i['Output'])
                            while choice:
                                # what do next?
                                choice_list = []
                                for i in Question_line:
                                    if i['Note'] == 'What you want to do':
                                        slowprint(i['Question'])
                                for i in Narrator_line:
                                    if i['Note'] == 'What you want to do':
                                        choice_list.append(i['Answer'])
                                choice_list.pop("Karczel's House")
                                choice_list.pop("Zahur’s room")
                                choice_list.pop("Omisha's room")
                                for i in range(len(choice_list)):
                                    print(f"{i}: {choice_list[i]}")
                                choose = input("Enter your choice: ")
                                for i in range(len(choice_list)):
                                    if choose == choice_list[i] or choose == str(i + 1):
                                        break
                                print('Wrong answer')
                            if choose.lower() == "the kitchen" or choose == '1':
                                # see zahur
                                for i in Narrator_line:
                                    if i['Note'] == 'What you want to do':
                                        if i['Answer'] == "The kitchen":
                                            slowprint(i['Output'])
                            slowprint("There's nothing else to do today.")
                        elif choose.lower() == "the kitchen" or choose == '1':
                            # see zahur
                            for i in Narrator_line:
                                if i['Note'] == 'What you want to do':
                                    if i['Answer'] == "The kitchen":
                                        slowprint(i['Output'])
                            while choice:
                                # what do next?
                                choice_list = []
                                for i in Question_line:
                                    if i['Note'] == 'What you want to do':
                                        slowprint(i['Question'])
                                for i in Narrator_line:
                                    if i['Note'] == 'What you want to do':
                                        choice_list.append(i['Answer'])
                                choice_list.pop("Karczel's House")
                                choice_list.pop("Zahur’s room")
                                choice_list.pop("The kitchen")
                                for i in range(len(choice_list)):
                                    print(f"{i}: {choice_list[i]}")
                                choose = input("Enter your choice: ")
                                for i in range(len(choice_list)):
                                    if choose == choice_list[i] or choose == str(i + 1):
                                        break
                                print('Wrong answer')
                            if choose.lower() == "omisha's room" or choose == '1':
                                # omisha
                                for i in Narrator_line:
                                    if i['Note'] == 'What you want to do':
                                        if i['Answer'] == "Omisha's room":
                                            slowprint(i['Output'])
                            slowprint("There's nothing else to do today.")

                    # do nothing(void)
                if choose.lower() == 'yes' or choose == '1':
                    # Yes
                    for i in Narrator_line:
                        if i['Note'] == 'See Karczel?':
                            if i['Answer'] == 'Yes':
                                slowprint(i['Output'])
                    while choice:
                        # clothing
                        choice_list = []
                        for i in Question_line:
                            if i['Note'] == 'Choose clothing':
                                slowprint(i['Question'])
                        for i in Narrator_line:
                            if i['Note'] == 'Choose clothing':
                                choice_list.append(i['Answer'])
                        for i in range(len(choice_list)):
                            print(f"{i}: {choice_list[i]}")
                        choose = input("Enter your choice: ")
                        for i in range(len(choice_list)):
                            if choose == choice_list[i] or choose == str(i + 1):
                                break
                    if choose.lower() == "karczel's clothes" or choose == '1':
                        # k
                        for i in S_c:
                            if i['clothing'] == "Over sized Karczel's Jacket":
                                sam.change_clothing(i['type'], i['clothing'])
                        for i in Narrator_line:
                            if i['Note'] == 'Choose clothing':
                                if i['Answer'] == "Karczel's Clothes":
                                    slowprint(i['Output'])

                    if choose.lower() == "karczel's handmade cloth" or choose == '2':
                        # k
                        for i in karczel.items:
                            sam.change_clothing(i['type'], i['clothing'])
                        for i in Narrator_line:
                            if i['Note'] == 'Choose clothing':
                                if i['Answer'] == "Karczel's Handmade Cloth":
                                    slowprint(i['Output'])
                        while choice:
                            # festival
                            choice_list = []
                            for i in Question_line:
                                if i['Note'] == 'Festival':
                                    slowprint(i['Question'])
                            for i in Narrator_line:
                                if i['Note'] == 'Festival':
                                    choice_list.append(i['Answer'])
                            for i in range(len(choice_list)):
                                print(f"{i}: {choice_list[i]}")
                            choose = input("Enter your choice: ")
                            for i in range(len(choice_list)):
                                if choose == choice_list[i] or choose == str(i + 1):
                                    break
                            print('Wrong answer')
                        if choose == 'The "Athleticmaton"' or choice == '1':
                            # robo stall
                            for i in Narrator_line:
                                if i['Note'] == 'Festival':
                                    if i['Answer'] == 'The "Athleticmaton"':
                                        slowprint(i['Output'])
                        elif choose == 'Virtual gun game' or choose == '2':
                            # gun stall
                            for i in Narrator_line:
                                if i['Note'] == 'Festival':
                                    if i['Answer'] == 'Virtual gun game':
                                        slowprint(i['Output'])
                        elif choose == 'Watch the tournament competition' or choose == '3':
                            # festival 3
                            for i in Narrator_line:
                                if i['Note'] == 'Festival':
                                    if i['Answer'] == 'Watch the tournament competition':
                                        slowprint(i['Output'])
                        for i in Narrator_line_extra:
                            if i['Note'] == 'Festival over late':
                                slowprint(i['Output'])
                        if 'suit' not in sam.clothing.values():
                            while choice:
                                # k dinner
                                choice_list = []
                                for i in Question_line:
                                    if i['Note'] == 'Karczel Dinner':
                                        slowprint(i['Question'])
                                for i in Narrator_line:
                                    if i['Note'] == 'Karczel Dinner':
                                        choice_list.append(i['Answer'])
                                for i in range(len(choice_list)):
                                    print(f"{i}: {choice_list[i]}")
                                choose = input("Enter your choice: ")
                                for i in range(len(choice_list)):
                                    if choose == choice_list[i] or choose == str(i + 1):
                                        break
                                print('Wrong answer')

                            if choose.lower() == 'yes' or choose == '1':
                                # k yes
                                for i in Narrator_line:
                                    if i['Note'] == 'Karczel Dinner':
                                        if i['Answer'] == 'Yes':
                                            slowprint(i['Output'])
                            elif choose.lower() == 'no' or choose == '2':
                                # k yes
                                for i in Narrator_line:
                                    if i['Note'] == 'Karczel Dinner':
                                        if i['Answer'] == 'No':
                                            slowprint(i['Output'])
                            elif choose.lower() == 'make the dinner' or choose == '3':
                                # k yes
                                for i in Narrator_line:
                                    if i['Note'] == 'Karczel Dinner':
                                        if i['Answer'] == 'Make the dinner':
                                            slowprint(i['Output'])
                        else:
                            while choice:
                                # fancy restaurant
                                choice_list = []
                                for i in Question_line:
                                    if i['Note'] == 'Food':
                                        slowprint(i['Question'])
                                for i in Narrator_line:
                                    if i['Note'] == 'Food':
                                        choice_list.append(i['Answer'])
                                for i in range(len(choice_list)):
                                    print(f"{i}: {choice_list[i]}")
                                choose = input("Enter your choice: ")
                                for i in range(len(choice_list)):
                                    if choose == choice_list[i] or choose == str(i + 1):
                                        break
                                print('Wrong answer')
                            for i in Narrator_line:
                                if i['Note'] =='Food':
                                    if i['Answer'] == 'Food1':
                                        slowprint(i['Output'])
                            while choice:
                                # dance
                                choice_list = []
                                for i in Question_line:
                                    if i['Note'] == 'Dance':
                                        slowprint(i['Question'])
                                for i in Narrator_line:
                                    if i['Note'] == 'Dance':
                                        choice_list.append(i['Answer'])
                                for i in range(len(choice_list)):
                                    print(f"{i}: {choice_list[i]}")
                                choose = input("Enter your choice: ")
                                for i in range(len(choice_list)):
                                    if choose == choice_list[i] or choose == str(i + 1):
                                        break
                                print('Wrong answer')
                            if choose.lower() == '"no"' or choose == '2':
                                # no
                                for i in Narrator_line:
                                    if i['Note'] == 'Dance':
                                        if i['Answer'] == '"No"':
                                            slowprint(i['Output'])

                            if choose.lower() == '"yes"' or choose == '1':
                                # no
                                for i in Narrator_line:
                                    if i['Note'] == 'Dance':
                                        if i['Answer'] == '"Yes"':
                                            slowprint(i['Output'])

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
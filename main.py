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
Narrator_line_extra = open("Story_Output/Narrator_line_extra adjustments.csv", encoding="utf8").read().splitlines()
f = [x.split(';') for x in Narrator_line_extra]
Narrator_line_extra = [{key: b[sub][idx] for idx, key in enumerate(f[0])}for sub in range(1,len(f))]

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
# print(Samantha_lines)
# print(Karczel_lines)
# print(Omisha_lines)
# print(Zahur_lines)
# print(Narrator_line)
# print(Question_line)
# print(Narrator_line_extra)

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
            if choose.lower() == 'another run' or choice == '1':
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
                    if choose == "Karczel's Clothes" or choose == '1':
                        # k
                        for i in Narrator_line:
                            if i['Note'] == 'Choose clothing':
                                if i['Answer'] == "Karczel's Clothes":
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
                    if choose == "Karczel's Handmade Cloth" or choose == '2':
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
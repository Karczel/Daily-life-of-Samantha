import sys,time,csv
def open_line_files(filename):
    line_list = open(filename).read().splitlines()
    b = [x.split(';') for x in line_list]
    c = b[0]
    line = {key: [sub[idx] for sub in line_list[1:]] for idx, key in enumerate(c)}
    return line

Narrator_line = open_line_files("Narrator_line.csv")
Samantha_line = open_line_files("Samantha_line.csv")
Karczel_line = open_line_files("Karczel_line.csv")
Omisha_line = open_line_files("Omisha_line.csv")
Zahur_line = open_line_files("Zahur_line.csv")
Person1_line = open_line_files("Person1.csv")

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
    return {key: [sub[idx] in clothing_list] for idx, key in enumerate(clothing_list[0])}


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
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


# class TurtleGraphi


sam = Samantha(,S_palette)

# arrange line functions and variable


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
import sys,time,csv

def open_line_files(filename):
    a = open(filename).read().splitlines()
    b = [x.split(',') for x in a]
    c = b[0]
    line = {key: [sub[idx] for sub in a[1:]] for idx, key in enumerate(c)}
    return line

Narrator_line = open_line_files("Narrator_line.csv")
Samantha_line = open_line_files("Samantha_line.csv")
Karczel_line = open_line_files("Karczel_line.csv")
Omisha_line = open_line_files("Omisha_line.csv")
Zahur_line = open_line_files("Zahur_line.csv")
Person1_line = open_line_files("Person1.csv")

def add_item(li_st, items):
    li_st.append(items)

def use_item(li_st,items):
    li_st.pop(items)

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

# requirement
# data = open("fguhaslirf.csv").read().splitlines()
# a = [Classname() for i in data]

# class TurtleGraphi


Samantha = Samantha()

# arrange line functions and variable

# --- Start ---
slowprint(Narrator_line[0])
input = False
while input == False:
    real_input = lower(input)
    if lowercase(input) == a or lowercase(input) == b:
else:
    print(f"Please type in one of the choices given: \n"
          f"{a} \n"
          f"{b}")
if real_input == a:
    while
elif real_input == b:
    while


# --- End ---
import sys,time,csv

N = open("Narrator_line.csv").read().splitlines()
N1 = [x.split(',')for x in N]
N_head = N[0]
Narrator_line = {key:[sub[idx] for sub in N[1:]] for idx, key in enumerate(N_head)}


S = open("Samantha_line.csv").read().splitlines()
S1 = [x.split(",") for x in S]
S_head = S1[0]
Samantha_line = {key:[sub[idx] for sub in S[1:]] for idx, key in enumerate(S_head)}

K = open("Karczel_line.csv").read().splitlines()
K1 = [x.split(',')for x in K]
K_head = K1[0]
Karczel_line = {key:[sub[idx] for sub in K[1:]] for idx, key in enumerate(K_head)}

O = open("Omisha_line.csv").read().splitlines()
O1 = [x.split(',')for x in O]
O_head = O1[0]
Omisha_line = {key:[sub[idx] for sub in O[1:]] for idx, key in enumerate(O_head)}


Z = open("Zahur_line.csv").read().splitlines()
Z1 = [x.split(',')for x in Z]
Z_head = K1[0]
Zahur_line = {key:[sub[idx] for sub in Z[1:]] for idx, key in enumerate(Z_head)}

P1 = open('Person1.csv').read().splitlines()
P11 = [x.split for x in P1]
P1_head = P1[0]
Person1_line = {key:[sub[idx] for sub in P1[1:]] for idx, key in enumerate(P1_head)}

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
    for i in s + '\n':
        a = character_name + ': ' + i
        sys.stdout.write(a)
        sys.stdout.flush()
        time.sleep(2./10)

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
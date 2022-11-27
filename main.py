import sys,time,csv

S = open("Samantha_line.csv").read().splitlines()
S1 = [x.split(",") for x in S]
S_head = S1[0]
Samantha_line = {key:[sub[idx] for sub in S[1:]] for idx, key in enumerate(S_head)}

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2./10)

class Samantha:
    def __init__(self):
        self. =

class Karczel:
    def __init__(self):

class Omisha:
    def __init__(self):

class Zahur:
    def __init__(self):

class Table:
    def __init__(self):

class Person:
    def __init__(self):

# --- Start ---
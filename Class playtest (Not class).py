import os
os.chdir('C:\Users\aumna\OneDrive\เอกสาร\GitHub\Daily-life-of-Samantha\Story_Output')
def open_character_line_files(filename):
    line_lists = open(filename).read().splitlines()
    line_split = [x.split(';') for x in line_lists]
    line = {texts[0]:[output for output in texts[1,len(texts-1)]] for texts in line_split}
    return line

Samantha_line = open_character_line_files("Samantha_line.csv")
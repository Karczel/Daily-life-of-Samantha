import sys
import time

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./10)
slowprint("Hello.")
# class Samantha:
#     def __init__(self):
#         self. =
#
# class Karczel:
#     def __init__(self):
#
# class Omisha:
#     def __init__(self):
#
# class Zahur:
#     def __init__(self):
#
# class Table:
#     def __init__(self):
#
# class Person:
#     def __init__(self):
#
# # --- Start ---
import string
import os

def gen_26_f():
    for el in string.ascii_uppercase:
        with open(f"{el}.txt", "w") as file:
            pass


gen_26_f()
import os

print("Current directory: ", os.getcwd())
print()
path = "/home/kali/my_project/urban-octo-memory/Lab6/2.3.py"
with open(path,"r", encoding = "utf-8") as file:
    lines = file.readlines()
print(f"Number of lines in file: {len(lines)}")
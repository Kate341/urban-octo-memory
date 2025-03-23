import os
print("Current directory: ", os.getcwd())
print()
path1 = "/home/kali/my_project/urban-octo-memory/Lab6/eee.txt"
path2 = "/home/kali/my_project/urban-octo-memory/Lab6/aaa.txt"
txt_file1 = open(path1,"r", encoding = "utf-8")
txt_file2 = open(path2, "w")

with open(path1, "r", encoding="utf-8") as txt_file1, open(path2, "w", encoding="utf-8") as txt_file2:
    txt_file2.write(txt_file1.read())
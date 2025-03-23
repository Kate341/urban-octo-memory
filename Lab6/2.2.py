import os

print("Current directory: ", os.getcwd())
print()
print(os.path.exists("/home/kali/my_project/urban-octo-memory/Lab6/1.5.py"))
print()
path = "/home/kali/my_project/urban-octo-memory/Lab6/1.5.py"
if os.path.exists(path):
    print(f"{path} exists")

    if os.access(path, os.R_OK):
        print(f"{path} is readable")
    else:
        print(f"{path} is NOT readable")

    if os.access(path, os.W_OK):
        print(f"{path} is writable")
    else:
        print(f"{path} is NOT writable")

    if os.access(path, os.X_OK):
        print(f"{path} is executable")
    else:
        print(f"{path} is NOT executable")
else:
    print(f"{path} does NOT exist")
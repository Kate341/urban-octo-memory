import os

print("Current directory: ", os.getcwd())
print()
path = "/home/kali/my_project/urban-octo-memory/Lab6/ddd.txt"
if os.path.isfile(path):
    if os.access(path, os.R_OK) and os.access(path, os.W_OK) and os.access(path, os.X_OK):
        os.remove(path)
        print(f"{path} has been removed.")
    else:
        print(f"Insufficient permissions to delete {path}.")
else:
    print(f"{path} does NOT exist")
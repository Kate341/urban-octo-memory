import os

print("Current directory: ", os.getcwd())
print()
path = "/home/kali/my_project/urban-octo-memory/Lab6"
if os.path.exists(path):
    if os.path.isdir(path):
        print(f"{path} is a directory")
        all_things = os.listdir(path)
        directories = [thing for thing in all_things if os.path.isdir(os.path.join(path, thing))]
        print("Directories: ", directories)
        print()
        files = [thing for thing in all_things if os.path.isfile(os.path.join(path, thing))]
        print("Files: ", files)
    elif os.path.isfile(path):
        print(f"{path} is a file")
    else:
        print(f"{path} exists but is neither a file nor a directory")
else:
    print(f"{path} does not exist")
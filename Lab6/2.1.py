import os

print("Current directory: ", os.getcwd())
print()
path = "."

all_things = os.listdir(path)

directories = [thing for thing in all_things if os.path.isdir(os.path.join(path, thing))]
print("Directories: ", directories)
print()
files = [thing for thing in all_things if os.path.isfile(os.path.join(path, thing))]
print("Files: ", files)
print()
print("All files and directories: ", all_things)
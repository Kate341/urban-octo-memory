import os
print("Current directory: ", os.getcwd())
print()
path = "/home/kali/my_project/urban-octo-memory/Lab6"

def write_list_to_file(list_it, path):
    with open(path, "w", encoding = "utf-8") as file:
        for it in list_it:
            file.write(f"{it}\n")
    print(f"List written to {path}")


write_list_to_file([1, 2, 3, 4, 5], './list_el.txt')
import re

txt = "my_favourite_language_is_english"
txt1 = "you_are_my_best_friend"

x = re.split("_", txt)
y = re.split("_", txt1)

x1 = "".join(x2.capitalize() for x2 in x)
y1 = "".join(y2.capitalize() for y2 in y)
print(x1)
print(y1)

#Without input()

txt2 = str(input())
z = re.split("_", txt2)
z1 = "".join(z2.capitalize() for z2 in z)

print(z1)

#With input()
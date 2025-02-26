import re

txt = "MyFavouriteLanguageIsEnglish"
txt1 = "YouAreMyBestFriend"

x = re.findall(r"[A-Z][a-z]*", txt)
y = re.findall(r"[A-Z][a-z]*", txt1)

x1 = " ".join(x2 for x2 in x)
y1 = " ".join(y2 for y2 in y)

print(x1)
print(y1)

#Without input()

txt2 = str(input())
z = re.findall(r"[A-Z][a-z]*", txt2)

z1 = " ".join(z2 for z2 in z)

print(z1)

#With input()
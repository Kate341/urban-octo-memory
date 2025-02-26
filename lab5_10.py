import re

txt = "MyFavouriteLanguageIsEnglish"
txt1 = "YouAreMyBestFriend"

x = re.findall("[A-Z][a-z]*", txt)
y = re.findall("[A-Z][a-z]*", txt1)

x1 = "_".join(x2.lower() for x2 in x)
y1 = "_".join(y2.lower() for y2 in y)

print(x1)
print(y1)

#Without input()

txt2 = str(input())
z = re.findall("[A-Z][a-z]*", txt2)

z1 = "_".join(z2.lower() for z2 in z)

print(z1)

#With input()
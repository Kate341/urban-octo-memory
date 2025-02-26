import re

txt = "MyFavouriteLanguageIsEnglish"
txt1 = "YouAreMyBestFriend"

x = re.findall(r"[A-Z][a-z]*", txt)
y = re.findall(r"[A-Z][a-z]*", txt1)

print(x)
print(y)

#Without input()

txt2 = str(input())
z = re.findall(r"[A-Z][a-z]*", txt2)

print(z)

#With input()
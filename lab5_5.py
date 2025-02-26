import re

txt = "arab arabica arabib arabics"
txt1 = "abbab abba adsdfab assswab"

x = re.findall("^a.*b$", txt)
y = re.findall("^a.*b$", txt1)

print(x)
print(y)


#Without input()

txt2 = str(input())

z = re.findall("^a.*b$", txt2)

print(z)

#With input()
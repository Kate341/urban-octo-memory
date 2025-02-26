import re

txt = "I really like My Sister"
txt1 = "You are a Student"

x = re.findall("[A-Z][a-z]+", txt)
y = re.findall("[A-Z][a-z]+", txt1)

print(x)
print(y)

print(bool(x))
print(bool(y))

#Without input()

txt2 = str(input())

z = re.findall("[A-Z][a-z]+", txt2)

print(z)
print(bool(z))

#With input()
import re

txt = "dfhgkfkdkv"
txt1 = "abba andromovo arcabaleno"

x = re.findall("ab*", txt)
y = re.findall("ab*", txt1)

print(x)
print(y)

print(bool(x))
print(bool(y))

if x:
    print("This string has an 'a' followed by zero or more 'b''s")
else:
    print("This string does not have an 'a' followed by zero or more 'b''s")

if y:
    print("This string has an 'a' followed by zero or more 'b''s")
else:
    print("This string does not have an 'a' followed by zero or more 'b''s")

#Without input()

txt2 = str(input())

z = re.findall("ab*", txt2)

print(z)
print(bool(z))

if y:
    print("This string has an 'a' followed by zero or more 'b''s")
else:
    print("This string does not have an 'a' followed by zero or more 'b''s")

#With input()
import re

txt = "dfhgkfkdkv"
txt1 = "abba andromovo arcabaleno"

x = re.findall("ab{2,3}", txt)
y = re.findall("ab{2,3}", txt1)

print(x)
print(y)

print(bool(x))
print(bool(y))

if x:
    print("This string has an 'a' followed by two to three 'b'")
else:
    print("This string does not have an 'a' followed by two to three 'b'")

if y:
    print("This string has an 'a' followed by two to three 'b'")
else:
    print("This string does not have an 'a' followed by two to three 'b'")

#Without input()

txt2 = str(input())

z = re.findall("ab{2,3}", txt2)

print(z)
print(bool(z))

if y:
    print("This string has an 'a' followed by two to three 'b'")
else:
    print("This string does not have an 'a' followed by two to three 'b'")

#With input()
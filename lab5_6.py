import re

txt = "I like speaking english, but i do not like writing english."
txt1 = "abbab, abba. adsdfab, assswab."

x = re.sub("[ .,]", ":", txt)
y = re.sub("[ .,]", ":", txt1)

print(x)
print(y)


#Without input()

txt2 = str(input())

z = re.sub("[ .,]", ":", txt2)

print(z)

#With input()
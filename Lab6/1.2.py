txt = "ajdgjgslgjdskldDSJJKFHSDKJHVKDajaddh"
def my_func1(txt):
    upper_letters = sum(1 for char in txt if char.isupper())
    lower_letters = sum(1 for char in txt if char.islower())
    
    print(f"Uppercase Letters: {upper_letters}")
    print(f"Lowercase Letters: {lower_letters}")

my_func1(txt)

#Without input()

text = str(input())

def my_func2(text):
    upper_letters = sum(1 for char in text if char.isupper())
    lower_letters = sum(1 for char in text if char.islower())
    
    print(f"Uppercase Letters: {upper_letters}")
    print(f"Lowercase Letters: {lower_letters}")

my_func2(text)

#With input()
x = [1, 2, 3]
def my_func(x):
    b = 1
    for num in x:
        b = eval('num * b')
    return b
y = my_func(x)
print(y)
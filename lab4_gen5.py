n = int(input())

def my_gen(n):
    value = n + 1
    while 0 < value:
        value -= 1
        yield value
print(", ".join(str(value) for value in my_gen(n)))
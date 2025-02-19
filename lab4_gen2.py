n = int(input())

def all_even(n):
    value = 0
    while value <= n:
        yield value
        value += 2

print(", ".join(str(value) for value in all_even(n)))
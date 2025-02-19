n = int(input())
def divisible_by_3_and_4(n):
    for value in range(n + 1):
        if value % 3 == 0 and value % 4 == 0:
            yield value

print(", ".join(str(value) for value in divisible_by_3_and_4(n)))
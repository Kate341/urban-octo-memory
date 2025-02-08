import math
import random
import itertools

grams = int(input())
def myfunction1(grams):
    ounces = grams * 28.3495231
    return ounces
print(myfunction1(grams))
#exercise 1

F = int(input())
def myfunction2(F):
    C = (5 / 9) * (F - 32)
    return C
print(myfunction2(F))
#exercise 2

numheads = int(input())
numlegs = int(input())
def solve(numheads, numlegs):
    for num_of_hens in range(numheads + 1):
        num_of_rabbits = numheads - num_of_hens
        if(num_of_hens * 2 + num_of_rabbits * 4) == numlegs:
            return num_of_hens, num_of_rabbits
print(solve(numheads, numlegs))
#exercise 3

def prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(num):
    return [number for number in num if prime(number)]

num = list(map(int,input().split()))
print(filter_prime(num))
#exercise 4


def permutation(s):
    permutation = itertools.permutations(s)
    
    for perm in permutation:
        print(''.join(perm))

s = input()
permutation(s)
#exersise 5



def rw(sentence):
    return ' '.join(sentence.split()[::-1])

s = input()
print(rw(s))
#exercise 6



def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

print(has_33([1,2,3,3,4,3]))
print(has_33([3,2,1,3,4,2,3]))
#exercise 7

def spy_game(nums):
    sequence = [0, 0, 7]
    for i in range(len(nums) - 2):
        if nums[i:i+3] == sequence:
            return True
    return False

print(spy_game([1,2,4,0,0,7,8]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))
#exercise 8

def sphere_volume(radius):
    return (4 / 3) * math.pi * radius ** 3

radius = float(input())
print(sphere_volume(radius))
#exercise 9

def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

numbers = [1, 2, 2, 3, 4, 3, 5, 1]
result = unique_elements(numbers)
print(result)
#exercise 10

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]


a = input()

if is_palindrome(a):
    print("Yes")
else:
    print("No")
#exercise 11

def histogram(lst):
    for num in lst:
        print('*' * num)

histogram([4,9,7])
#exercise 12

def guess_number():
    print("Hello! What is your name?")
    n = input()

    a = random.randint(1, 20)
    print("Well,", n, "I am thinking of a number between 1 and 20.")

    cnt = 0

    while True:
        cnt += 1
        q = int(input("Take a guess.\n"))

        if q == 0:
            print("Number is", a)
            break

        if q < a:
            print("Your guess is too low.")
        elif q > a:
            print("Your guess is too high.")
        else:
            print("Good job,", n, "! You guessed my number in", cnt, "guesses!")
            break
#exercise 13






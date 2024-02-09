import math
from itertools import permutations
from random import random, randint


def recipe(grams):
    return 28.3495231 * grams


def farenheit(temp):
    celsius = (5 / 9) * (temp - 32)
    return celsius


def solve(numheads, numlegs):
    for i in range(numheads + 1):
        rabbits = numheads - i
        if (2 * i + 4 * rabbits) == numlegs:
            print(f'Chickens: {i}')
            print(f'Rabbits: {rabbits}')


def filter_prime(l):
    def is_prime(a):
        for i in range(2, a):
            if not a % i:
                return False
        return True

    return list(filter(lambda x: is_prime(x), l))


def permutation(string):
    print([''.join(i) for i in list(permutations(string))])


def reverse(string):
    return ' '.join(string.split()[::-1])


def has_33(nums):
    for i in range(0, len(nums) - 1):
        if nums[i] == nums[i + 1] == 3:
            return True
    return False


def spy_game(nums):
    nums_ = list(filter(lambda x: x == 0 or x == 7, nums))
    for i in range(0, len(nums_) - 2):
        if nums_[i] == nums_[i + 1] == 0 and nums_[i + 2] == 7:
            return True
    return False


def sphere(r):
    return 4 * math.pi * (r ** 3) / 3


def unique(l):
    dic = {i: [] for i in l}
    return list(dic.keys())


def palindrome(string):
    return string == string[::-1]


def histogram(lis):
    return ['*' * i + '\n' for i in lis]


def game():
    num = randint(1, 20)
    print('Hello! What is your name?')
    name = input()
    print(f'Well, {name}, I am thinking of a number between 1 and 20.')
    print('Take a guess.')
    k = 1
    guessed = False
    guessing = int(input())
    if guessing > num:
        print('Your guess is too high.')
        print('Take a guess.')
    elif guessing < num:
        print('Your guess is too low.')
        print('Take a guess.')
    else:
        print(f'Good job, KBTU! You guessed my number in {k} guesses!')
        guessed = True
    while True and not guessed:
        guessing = int(input())
        if guessing > num:
            print('Your guess is too high.')
            print('Take a guess.')
        elif guessing < num:
            print('Your guess is too low.')
            print('Take a guess.')
        else:
            print(f'Good job, KBTU! You guessed my number in {k} guesses!')
            break
        k += 1

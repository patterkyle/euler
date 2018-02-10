# Smallest multiple Problem 5

# 2520 is the smallest number that can be divided by each of the
# numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20?

import itertools

def is_divisible(a, b):
    return a % b == 0

def main():
    for x in itertools.count(1):
        if all(is_divisible(x, y) for y in range(1, 21)):
            return x

if __name__ == '__main__':
    print(main())

# Largest prime factor
# Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

from math import sqrt

def is_divisible(a, b):
    return a % b == 0

def is_prime(n):
    if n < 2:
        return False
    for x in range(2, int(sqrt(n))+1):
        if is_divisible(n, x):
            return False
    return True

def prime_factors(n):
    for x in range(2, int(sqrt(n))+1):
        if is_divisible(n, x) and is_prime(x):
            yield x

def main(n):
    return max(prime_factors(n))

if __name__ == '__main__':
    print(main(600851475143))

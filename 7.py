# 10001st prime Problem 7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we
# can see that the 6th prime is 13.

# What is the 10 001st prime number?

from math import sqrt
import itertools

def is_prime(n):
    if n < 2:
        return False
    for x in range(2, int(sqrt(n))+1):
        if n % x == 0:
            return False
    return True

def primes():
    while True:
        for i in itertools.count(1):
            if is_prime(i):
                yield i

def nth_prime(n):
    if n < 1:
        raise ValueError('n must be positive.')
    p = primes()
    while n > 1:
        next(p)
        n -= 1
    return next(p)

if __name__ == '__main__':
    print(nth_prime(10001))

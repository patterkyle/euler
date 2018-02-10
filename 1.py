# Multiples of 3 and 5
# Problem 1

# If we list all the natural numbers below 10 that are multiples of 3
# or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

def is_divisible(m, n):
    'Returns True if m is evenly divisible by n.'
    return m % n == 0

def main():
    return sum(x for x in range(1000)
               if is_divisible(x, 3) or is_divisible(x, 5))

if __name__ == '__main__':
    print(main())

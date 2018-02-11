# Sum square difference
# Problem 6

# The sum of the squares of the first ten natural numbers is,
# 1**2 + 2**2 + ... + 10**2 = 385

# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)**2 = 552 = 3025

# Hence the difference between the sum of the squares of the first ten
# natural numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.

def sum_of_squares(n):
    return sum(x*x for x in range(1, n+1))

def square_of_sums(n):
    range_sum = sum(range(n+1))
    return range_sum * range_sum

def main(n):
    return abs(sum_of_squares(n) - square_of_sums(n))

if __name__ == '__main__':
    print(main(100))

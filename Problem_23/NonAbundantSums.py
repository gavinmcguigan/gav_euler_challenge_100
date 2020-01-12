from globs import *
from math import sqrt
"""
    A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
    For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28
    is a perfect number.

    A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if
    this sum exceeds n.

    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the
    sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123
    can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by
    analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant
    numbers is less than this limit.

    Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""


def attempt2(num):
    a = [n for n in range(int(sqrt(num)), 0, -1) if not num % n]
    print(a)


def get_sum_of_divisors2(num):
    divisors = []
    for n in range(int(sqrt(num)), 0, -1):
        if not num % n:
            divisors.append(n)
            result = num // n
            if result != n and result != num:
                divisors.append(result)

    return sum(divisors)


def go():
    # abundants = [num for num in range(1, 28124) if (sum([n for n in range(num // 2, 0, -1) if not num % n])) > num]
    abundants = [i for i in range(28124) if get_sum_of_divisors2(i) > i]
    return sum({i for i in range(1, 28124)} - {i + j for i in abundants for j in abundants if (i + j) < 28124})


if __name__ == '__main__':
    answer = go()
    print(f'Answer: {answer} in {get_time_running():0.4f} secs')

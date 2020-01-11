from math import sqrt
"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called 
amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""

AMICABLE_SUM = 0


def get_sum_of_divisors(num):
    divisors = []
    for n in range(num // 2, 0, -1):
        if not num % n:
            divisors.append(n)
    return sum(divisors)


def go():
    amicable_sum = 0
    for i in range(1, 10000):
        sumdivs1 = get_sum_of_divisors(i)
        if sumdivs1 != i and get_sum_of_divisors(sumdivs1) == i:
            amicable_sum += i
    return amicable_sum


if __name__ == '__main__':
    answer = go()
    print(f'Answer: {answer}')
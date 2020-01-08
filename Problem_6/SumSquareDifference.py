"""
The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10*2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of
the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""


def calc_sum_sq_diff(n: int = 10) -> int:
    tot1, tot2 = 0, 0
    for s in range(n, 0, -1):
        tot1 += s**2
        tot2 += s

    return tot2**2 - tot1


if __name__ == '__main__':
    answer = calc_sum_sq_diff(100)
    print(f"Answer: {answer}")

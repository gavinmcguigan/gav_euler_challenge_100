from globs import *

"""
    A googol (10**100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably 
    large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

    Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
"""


def check_all_powers_in_range(a: int) -> int:
    largest = 0
    for b in range(1, 100):
        p = str(pow(a, b))
        s = 0
        for d in p:
            s += int(d)
        if s > largest:
            largest = s

    return largest


def main() -> int:
    max_sum_of_digits = 0
    for a in range(100):
        sum_of_digits = check_all_powers_in_range(a)

        if sum_of_digits > max_sum_of_digits:
            max_sum_of_digits = sum_of_digits

    return max_sum_of_digits


if __name__ == '__main__':
    answer = main()
    show_answer(answer)

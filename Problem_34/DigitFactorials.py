from globs import *

"""
    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

    Find the sum of all numbers which are equal to the sum of the factorial of their digits.
    
    Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""


def get_digits(num, f):
    val = [int(y) for y in list(str(num))]
    total = 0
    for v in val:
        result = f[v]
        total += result

    return num if total == num else False


def start():
    facts = {0: 1}
    product = 1
    for i in range(1, 10):
        product *= i
        facts[i] = product

    upper = 7 * facts[9]
    total = 0
    for n in range(3, upper):
        ok = get_digits(n, facts)
        if ok:
            EULER_LOGGER.debug(f"->  {n}")
            total += n

    return total


if __name__ == '__main__':
    answer = start()
    show_answer(answer)

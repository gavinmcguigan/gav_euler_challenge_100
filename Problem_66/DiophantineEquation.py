from globs import *

"""
    Consider quadratic Diophantine equations of the form:

    x**2 – Dy**2 = 1
    
    For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.
    
    It can be assumed that there are no solutions in positive integers when D is square.
    
    By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:
    
    3**2 – 2×2**2 = 1
    2**2 – 3×1**2 = 1
    9**2 – 5×4**2 = 1
    5**2 – 6×2**2 = 1
    8**2 – 7×3**2 = 1
    
    Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.
    
    Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.
"""


def gen_convergents(i: float):
    """ Generates convergents up until the end of the period. """

    n = Decimal(i).sqrt()
    t = Decimal(i).sqrt()
    limit = 2 * int(t)

    while True:
        a, b = int(n), n - floor(n)
        yield a
        n = 1/b

        if a >= limit:
            break


def calc__continued_fraction(j: int) -> int:
    """ Gets period of convergents for the square root of j
        Calculates the continued fraction terms and returns the denominator
    """

    cons = [i for i in gen_convergents(j)][:-1]
    length_x = len(cons)

    num = cons.pop()
    den = 1

    while cons:
        num, den = num*cons.pop() + den, num

    if length_x % 2 != 0:
        num, den = 2*num**2 + 1, 2*num*den

    return num


def main():
    largest_num = 0
    i_for_largest_num = None
    for i in [g for g in range(2, 1001) if not sqrt(g).is_integer()]:
        n = calc__continued_fraction(i)

        if n > largest_num:
            largest_num = n
            i_for_largest_num = i

    return i_for_largest_num


if __name__ == '__main__':
    answer = main()
    show_answer(answer)
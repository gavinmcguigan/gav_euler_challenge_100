from globs import *

"""
    The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it 
    may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

    We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

    There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing 
    two digits in the numerator and denominator.

    If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

"""


def gen_num_doms():
    for i in range(11, 100):
        for j in range(i + 1, 100):
            if not i % 10 and not j % 10:
                continue

            s1 = list(str(i))
            s2 = list(str(j))

            s3 = []
            for each in s1:
                if each not in s2:
                    s3.append(each)

            for each in s2:
                if each not in s1:
                    s3.append(each)

            s3 = [int(x) for x in s3]

            if len(s3) == 2 and s3[0] < s3[1] and i/j == s3[0]/s3[1]:
                yield i, j, i/j, s3[0], s3[1]


def start():
    g = gen_num_doms()
    num = 1
    dom = 1
    for n, (a, b, c, d, e) in enumerate(g):
        EULER_LOGGER.debug(f"{n} ->  {a} / {b} = {c:<5}  - >  {d} / {e} = {d/e}")
        num *= d
        dom *= e

    a = None
    g2 = gen_get_divisors(num)
    for i in g2:
        if not dom % i:
            EULER_LOGGER.debug(f"{i} is the highest common divisor of both {num} and {dom}.")
            a = i
            break

    return dom//a


if __name__ == '__main__':
    answer = start()
    show_answer(answer)

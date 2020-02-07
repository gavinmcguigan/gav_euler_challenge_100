from globs import *
from math import e

"""
    Hence the sequence of the first ten convergents for 2–√ are:

    1,3/2,7/5,17/12,41/29,99/70,239/169,577/408,1393/985,3363/2378,...
    What is most surprising is that the important mathematical constant,
    e=[2;1,2,1,1,4,1,1,6,1,...,1,2k,1,...].
    
    The first ten terms in the sequence of convergents for e are:
    
    2,3,8/3,11/4,19/7,87/32,106/39,193/71,1264/465,1457/536,...
    The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.
    
    Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.
"""


def calc_seq_of_e(seq: list, n: float = e, inc: int = 0, ):
    """ after about 20 iterations, because we're dealing with floats, the seq values aren't as I'd expect. """
    inc += 1

    a, b = int(n), n - floor(n)
    seq.append(a)

    if inc == 102:          # For rational numbers, b == 0 when they terminate. For e, it never terminates...
        return
    else:
        calc_seq_of_e(seq, 1/b, inc)

    return seq


def calc_numerator_of_e(term: int = 10):
    seq = [(i // 3 * 2) if i % 3 == 1 else 1 for i in range(term + 2)]
    p, q = [1, 1], [1, 0]

    for n, a in enumerate(seq):
        if n < 2:
            continue

        p_actual = a * p[n - 1] + p[n - 2]
        p.append(p_actual)

        q_actual = a * q[n - 1] + q[n - 2]
        q.append(q_actual)

        # EULER_LOGGER.debug(f"{n-2:<8}{p_actual:<15} / {q_actual}")

    return p[-1]


def main():
    num = calc_numerator_of_e(100)
    return sum(int(i) for i in str(num))


if __name__ == '__main__':
    answer = main()
    show_answer(answer)

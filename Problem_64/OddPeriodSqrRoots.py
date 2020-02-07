from globs import *

"""
    All square roots are periodic when written as continued fractions and can be written in the form:

    N−−√=a0+1a1+1a2+1a3+…
    For example, let us consider 23−−√:23−−√=4+23−−√−4=4+1123√−4=4+11+23√−37
    If we continue we would get the following expansion:
    
    23−−√=4+11+13+11+18+…
    The process can be summarised as follows:
    
    a0=4,123√−4=23√+47=1+23√−37
    a1=1,723√−3=7(23√+3)14=3+23√−32
    a2=3,223√−3=2(23√+3)14=1+23√−47
    a3=1,723√−4=7(23√+4)7=8+23−−√−4
    a4=8,123√−4=23√+47=1+23√−37
    a5=1,723√−3=7(23√+3)14=3+23√−32
    a6=3,223√−3=2(23√+3)14=1+23√−47
    a7=1,723√−4=7(23√+4)7=8+23−−√−4
    It can be seen that the sequence is repeating. For conciseness, we use the notation 23−−√=[4;(1,3,1,8)], 
    to indicate that the block (1,3,1,8) repeats indefinitely.
    
    The first ten continued fraction representations of (irrational) square roots are:
    
    2–√=[1;(2)], period=1
    3–√=[1;(1,2)], period=2
    5–√=[2;(4)], period=1
    6–√=[2;(2,4)], period=2
    7–√=[2;(1,1,1,4)], period=4
    8–√=[2;(1,4)], period=2
    10−−√=[3;(6)], period=1
    11−−√=[3;(3,6)], period=2
    12−−√=[3;(2,6)], period=2
    13−−√=[3;(1,1,1,1,6)], period=5
    
    Exactly four continued fractions, for N≤13, have an odd period.
    
    How many continued fractions for N≤10000 have an odd period?
"""


def calculate(n):
    a0, a, m, d = int(sqrt(n)), int(sqrt(n)), 0, 1
    counter = 0
    while a < 2 * a0:
        m = d * a - m
        d = (n - m ** 2) / d
        y = (a0 + m) / d
        a = int(y)
        counter += 1
        # EULER_LOGGER.debug(f"{a:<10} {y}")

    return counter % 2


def main():
    odds = 0
    for i in [y for y in range(2, 10001) if not sqrt(y).is_integer()]:
        odds += calculate(i)

    return odds


if __name__ == '__main__':
    answer = main()
    show_answer(answer)

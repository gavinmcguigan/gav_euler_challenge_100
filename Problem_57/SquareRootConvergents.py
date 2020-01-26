from globs import *

"""
    It is possible to show that the square root of two can be expressed as an infinite continued fraction.

    √2 = 1 + 1/2 + 1/(2+1/2) + … 
    By expanding this for the first four iterations, we get:
    
    1 + 1/2 = 3/2 = 1.5
    1 + 1/(2 + 1/2) = 7/5 = 1.4
    1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666…
    1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379…
    
    The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example 
    where the number of digits in the numerator exceeds the number of digits in the denominator.
    
    In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?
"""


def gen_convergents(limit: int = 1000):
    numerator, denominator, inc = 1, 2, 1
    while inc < limit:
        numerator, denominator = denominator, (2*denominator) + numerator
        n, d = numerator + denominator, denominator
        if len(str(n)) > len(str(d)):
            yield n, d
        inc += 1


def main():
    g = gen_convergents()
    count = 0
    for n, d in g:
        count += 1

    return count


if __name__ == '__main__':
    answer = main()
    show_answer(answer)

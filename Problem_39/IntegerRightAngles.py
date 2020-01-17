from globs import *

"""
    If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are 
    exactly three solutions for p = 120.

    {20,48,52}, {24,45,51}, {30,40,50}

    For which value of p ≤ 1000, is the number of solutions maximised?
    
"""


def main():
    """
        As C > B and B >= A, the lower limit for C has to be 1 more than 1000/3.
        I've put a high limit of 500. This way the max values you could get for A & B would be 499 & 1,
        which when you apply pythagoras,  A**2 + B**2 < C**2 by almost 1000.  (249001 + 1 < 250000)
    """

    results, a, r = {}, None, 0

    for c in range(500, 334, -1):
        for b in range(c - 2, 3, -1):
            a = sqrt(c**2 - b**2)
            if a.is_integer():
                p = a + b + c
                t = results.get(p, None)
                results[p] = 1 if t is None else results[p] + 1

    for k, v in results.items():
        if v > r:
            a, r = k, v

    return int(a)


if __name__ == '__main__':
    answer = main()
    show_answer(answer)

from math import sqrt

"""
    A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators
    2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1
    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit
    recurring cycle.

    Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

# Largest reptend prime in range will have the largest cyclic number.


def get_primes_backwards_in_range(r: int):
    for i in range(r, 1, -1):
        top_val = sqrt(i)
        if not top_val.is_integer():
            top_val = int(top_val)
            if not top_val % 2:
                top_val -= 1

            for n in range(top_val, 1, -2):
                if not i % n:
                    break
            else:
                if i % 2:
                    yield i
    yield 2


def get_reptend_primes(n: int):
    g = get_primes_backwards_in_range(n)

    if n < 8:
        return 3

    for d in g:
        for i in range(1, n):
            if pow(10, i) % d == 1:
                if d - 1 == i:
                    yield d
                else:
                    break


if __name__ == '__main__':
    g = get_reptend_primes(1000)
    print(f"Answer: {g.__next__()}")


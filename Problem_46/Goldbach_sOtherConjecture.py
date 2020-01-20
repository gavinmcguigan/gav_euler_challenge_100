from globs import *

"""
    It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a 
    prime and twice a square.

    9 = 7 + 2×1**2
    15 = 7 + 2×2**2
    21 = 3 + 2×3**2
    25 = 7 + 2×3**2
    27 = 19 + 2×2**2
    33 = 31 + 2×1**2
    
    It turns out that the conjecture was false.
    What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""


def gen_pop_number_from_list():
    num_list = {n for n in range(1, 10000) if n % 2}
    y = None
    while True:
        recd = (yield y)
        try:
            num_list.remove(recd)
        except KeyError:
            pass

        y = min(num_list)


def main():
    g = gen_pop_number_from_list()
    g.send(None)

    found, a = False, None
    prime_gen = gen_primes(start=1, end=10000)
    for p in prime_gen:
        for y in range(50):
            r = g.send(p + 2 * (y ** 2))
            if r < p:
                a = r
                found = True
                break
        if found:
            break
    return a


if __name__ == '__main__':
    answer = main()
    show_answer(answer)

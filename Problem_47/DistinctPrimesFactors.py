from globs import *

"""
    The first two consecutive numbers to have two distinct prime factors are:

    14 = 2 × 7
    15 = 3 × 5
    
    The first three consecutive numbers to have three distinct prime factors are:
    
    644 = 2² × 7 × 23
    645 = 3 × 5 × 43
    646 = 2 × 17 × 19.
    
    Find the first four consecutive integers to have four distinct prime factors 
    each. What is the first of these numbers?

"""


def main():
    consecutive_count = []
    for i in range(1000, 150000):
        g = gen_get_divisors(i)
        count = 0
        for n in g:
            if is_prime(n):
                count += 1

        if count == 4:
            consecutive_count.append(i)
        else:
            consecutive_count = []

        if len(consecutive_count) == 4:
            break

    return consecutive_count[0]


if __name__ == '__main__':
    answer = main()
    show_answer(answer)

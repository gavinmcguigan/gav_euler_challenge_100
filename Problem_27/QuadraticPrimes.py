from globs import *
"""
    Euler discovered the remarkable quadratic formula:

        n2+n+41

    It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However,
    when n=40,40**2+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,41**2+41+41 is clearly
    divisible by 41.

    The incredible formula

        n2−79n+1601

    was discovered, which produces 80 primes for the consecutive values 0≤ n ≤79.
    The product of the coefficients, −79 and 1601, is −126479.

    Considering quadratics of the form:

    n**2+an+b, where |a|<1000 and |b|≤1000

    where |n| is the modulus/absolute value of n
    e.g. |11|=11 and |−4|=4

    Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number
    of primes for consecutive values of n, starting with n=0.

"""


def euler_formula():
    for n in range(0, 41):
        result = n**2 + n + 41
        is_it_a_prime = is_prime(result)
        EULER_LOGGER.debug(f"{result:<6} Prime? {is_it_a_prime} ")


def second_formula():
    for n in range(0, 81):
        result = n**2 - 79*n + 1601
        is_it_a_prime = is_prime(result)
        EULER_LOGGER.debug(f"{result:<6} Prime? {is_it_a_prime} ")


def tuple_gen():
    for a in range(-999, 1000, 2):
        for b in range(-1000, 1001):
            if is_prime(b):
                yield a, b


def quad_form():
    gen = tuple_gen()
    consecutive_primes, x, y = 0, 0, 0

    for e, (a, b) in enumerate(gen):
        t = 0
        for n in range(100):
            r = n**2 + a*n + b
            if is_prime(r):
                t += 1
            else:
                break

        if t > consecutive_primes:
            consecutive_primes = t
            x, y = a, b

    EULER_LOGGER.debug(f"For a= {x} b= {y}, you get {consecutive_primes} consecutive primes.")
    show_answer(x*y)


if __name__ == '__main__':
    quad_form()
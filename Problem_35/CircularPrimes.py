from globs import *

"""
    The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, 
    are themselves prime.

    There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
    
    How many circular primes are there below one million?
         
"""


def combos(j):
    i = str(j)
    for item in list(permutations(i, len(i))):
        s = int(''.join(item))
        EULER_LOGGER.debug(f"{item} -> {is_prime(s)}")


def gen_rotate(s):
    """ Rotates the string until it reaches the same one that it started with. """
    c = s
    while True:
        s = s[1:] + s[:1]
        if s == c:
            break
        else:
            yield int(s)


def check_if_circular(i):
    """ Checks if the prime number it receives + all of it's circular versions are prime.
    Returns True if they are and False if not.
    """

    g = gen_rotate(i)
    for item in g:
        if not is_prime(item):
            break
    else:
        return True

    return False


def start():
    """ Gets prime numbers between the limits specified from a generator in globs.py.
        Calls check_if_circular and if it returns True, the Total found is incremented.
    """
    total = 0
    g = gen_primes(low_limit=2, high_limit=999999)
    for i in g:
        if check_if_circular(str(i)):
            total += 1

    return total


if __name__ == '__main__':
    answer = start()
    show_answer(answer)

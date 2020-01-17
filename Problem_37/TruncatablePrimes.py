from globs import *

"""
    The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits 
    from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to 
    left: 3797, 379, 37, and 3.

    Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
    
    NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.


"""


def prime_is_truncatable(p):

    def looper(original_str, from_left=True):
        for n, num in enumerate(original_str[:-1]):
            check_this = original_str[n + 1:] if from_left else original_str[:-1 - n]
            if not is_prime(int(check_this)):
                break
        else:
            return True
        return False

    if looper(p):               # Removes from left
        if looper(p, False):    # Removes from right
            return True
    return False


def start():
    total = 0
    found = 0
    g = gen_primes(10, 1000000)

    for prime in g:
        if prime_is_truncatable(str(prime)):
            total += prime
            found += 1
            EULER_LOGGER.debug(f"This is one --->   {prime}")
            if found == 11:
                break
    return total


if __name__ == '__main__':
    answer = start()
    show_answer(answer)

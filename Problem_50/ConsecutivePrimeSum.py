from globs import *

"""
    The prime 41, can be written as the sum of six consecutive primes:

    41 = 2 + 3 + 5 + 7 + 11 + 13
    This is the longest sum of consecutive primes that adds to a prime below one-hundred.
    
    The longest sum of consecutive primes below one-thousand that adds to a prime, 
    contains 21 terms, and is equal to 953.
    
    Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""


def search_through_prime_sums(alist: list):
    """
    Work backwards from prime sums in first loop and in second loop, we subtract from first element
    to the number in first loop. If the result of the subtraction is a prime, break from the loop,
    we have the answer.  
    """
    a, c = None, None

    for i in alist[-1: 0: -1]:
        list2 = alist.copy()
        while True:
            j = list2.pop(0)
            a = i - j
            if is_prime(a):
                c = len(list2)
                found = True
                break
        if found:
            break
    return a, c


def main():
    """ Generate a list of prime sums. """
    prime_sums = []
    s = 0
    for g in gen_primes(1, 5000):
        s += g
        if s > 1000000:
            break
        else:
            prime_sums.append(s)

    a, c = search_through_prime_sums(prime_sums)

    return f"{a}"


if __name__ == '__main__':
    answer = main()
    show_answer(answer)

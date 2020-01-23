from globs import *

"""
    By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible 
    values: 13, 23, 43, 53, 73, and 83, are all prime.

    By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example 
    having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 
    56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with 
    this property.

    Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the 
    same digit, is part of an eight prime value family.
"""


def check_if_has_3_repeated_digits(prime: str) -> (str, list):
    """ Checks if there are 3 digits the same.  returns the repeating digit and its indices. """
    num_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    for digit in prime:
        num_dict[int(digit)] += 1

    for k, v in num_dict.items():
        if v > 2:
            repeating_digit = k
            indices = [i for i, x in enumerate(prime) if int(x) == repeating_digit]
            break
    else:
        return None, None

    return str(repeating_digit), indices


def check_for_family_of_primes(r: str, ind: list, p: list) -> list:
    """ Check if by replacing the repeating digit with the other 9 possible digits, how many are primes.
    we return a list of those which are.
    """
    values_to_check = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    values_to_check.remove(r)

    counter = ["".join(p)]
    for d in values_to_check:
        p[ind[0]] = d
        p[ind[1]] = d
        p[ind[2]] = d

        if is_prime(int("".join(p))):
            counter.append("".join(p))

    return [int(i) for i in counter]


def main() -> int:
    """ Generate prime numbers and pass to the other two functions.  If we find a family of 8 primes, we break
    and return the answer.
    """

    a = None
    for n, g in enumerate(gen_primes(100000, 1000000)):
        repeat, indices = check_if_has_3_repeated_digits(str(g))
        if repeat:
            a = check_for_family_of_primes(repeat, indices, list(str(g)))
            if len(a) > 7 and min(a) > 100000:
                EULER_LOGGER.debug(f"{a}")
                a = min([int(i) for i in a])
                break

    return a


if __name__ == '__main__':
    answer = main()
    show_answer(answer)

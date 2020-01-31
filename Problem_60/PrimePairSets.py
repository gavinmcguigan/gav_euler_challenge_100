from globs import *

"""
    The primes 3, 7, 109, 673 are quite remarkable. By taking any two primes and concatenating them in any order the
    result will always be prime.  For example, taking 7 and 109, both 7109 and 1097 are prime.  The sum of these four 
    primes, 792 represents the lowest sum for a set of four primes with this property. 
    
    Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime. 
"""
UPPER_LIMIT = 10000
PRIMES_LIST = list(gen_primes(3, UPPER_LIMIT))


def check_for_five(list_of_lists: list):
    list_5_primes = []
    for a, b, c, d in list_of_lists:
        i = PRIMES_LIST.index(d)
        for p in PRIMES_LIST[i + 1:]:
            if check_concats(a, p):
                if check_concats(b, p):
                    if check_concats(c, p):
                        if check_concats(d, p):
                            list_5_primes.append([a, b, c, d, p])

    EULER_LOGGER.debug(f"5 -> {list(list_5_primes)}")


def check_for_four(list_of_lists: list):
    list_4_primes = []
    for a, b, c in list_of_lists:
        i = PRIMES_LIST.index(c)
        for p in PRIMES_LIST[i + 1:]:
            if check_concats(a, p):
                if check_concats(b, p):
                    if check_concats(c, p):
                        list_4_primes.append([a, b, c, p])

    EULER_LOGGER.debug(f"4 ->  {len(list(list_4_primes))}")
    check_for_five(list_4_primes)


def check_for_three(list_of_lists: list):
    list_3_primes = []
    for a, b in list_of_lists:
        i = PRIMES_LIST.index(b)
        for p in PRIMES_LIST[i + 1:]:
            if check_concats(a, p):
                if check_concats(b, p):
                    list_3_primes.append([a, b, p])

    EULER_LOGGER.debug(f"3 ->  {len(list(list_3_primes))}")
    check_for_four(list_3_primes)


def check_for_two():
    list_2_primes = []
    for first in PRIMES_LIST:
        i = PRIMES_LIST.index(first)
        for second in PRIMES_LIST[i + 1:]:
            if check_concats(first, second):
                list_2_primes.append([first, second])

    EULER_LOGGER.debug(f"2 ->  {len(list(list_2_primes))}")
    check_for_three(list_2_primes)


def check_concats(a: int, b: int) -> bool:
    if is_prime(int(str(a) + str(b))):
        if is_prime(int(str(b) + str(a))):
            return True

    return False


def main():
    check_for_two()
    return False


if __name__ == '__main__':
    answer = main()
    show_answer(answer)



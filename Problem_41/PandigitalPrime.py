from globs import *

"""
    We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. 
    For example, 2143 is a 4-digit pandigital and is also prime.

    What is the largest n-digit pandigital prime that exists?
"""


def gen_permutations(seed):
    a = permutations(seed, len(seed))
    for each in a:
        v = int("".join(each))
        if is_prime(v):
            yield v


def check_if_multiple_of_3():
    s = ['987654321', '87654321', '7654321', '654321', '54321', '4321', '321', '21']

    new_s = []

    for seed in s:
        a = permutations(seed, len(seed))
        for p in a:
            if int("".join(p)) % 3:
                new_s.append(seed)
                break

    return new_s


def main():
    s = check_if_multiple_of_3()        # s = ['7654321', '4321']
    a, found = None, False

    for num in s:
        g = gen_permutations(num)
        for p in g:
            a = p
            found = True
            break

        if found:
            break

        EULER_LOGGER.debug(f"{get_time_running():0.4f} secs")

    return a


if __name__ == '__main__':
    answer = main()
    show_answer(answer)

from globs import *

"""
    We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for 
    example, the 5-digit number, 15234, is 1 through 5 pandigital.

    The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product 
    is 1 through 9 pandigital.
    
    Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 
    9 pandigital.
    
    HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""


def give_me_pairs() -> tuple:
    """ Only loop through these combinations
            2digits * 3digits = 4digits
            1digit * 4digits = 4digits
    """
    st = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

    for i in range(1, 100):
        m, n = (1000, 10000//i + 1) if i < 10 else (100, 9999//i + 1)
        for j in range(m, n):
            r = i * j
            s = f"{i}{j}{r}"
            if len(s) == 9:
                if not len(st.difference(set(s))):
                    yield i, j, r


def start():
    result_list = []
    g = give_me_pairs()
    for t, u, v in g:
        EULER_LOGGER.debug(f"{t} * {u} = {v}")
        result_list.append(v)

    return sum(set(result_list))


if __name__ == '__main__':
    answer = start()
    show_answer(answer)

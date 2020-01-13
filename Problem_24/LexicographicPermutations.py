from globs import *

"""
    A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 
    1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
    The lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

    What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

"""


def part2(val, indx):
    for mi in reversed(val):
        indx2 = val.index(mi)
        if not (mi <= val[indx - 1]):
            val[indx - 1], val[indx2] = val[indx2], val[indx - 1]
            val[indx:] = val[-1: indx - 1: -1]
            return val


def part1(val):
    for mi in reversed(val):
        indx = val.index(mi)
        if not (indx > 0 and val[indx - 1] >= val[indx]):
            if indx != 0:
                answer = part2(val, indx)
                break
    else:
        return False

    return answer


if __name__ == '__main__':
    lex_perm = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    counter = 1
    while lex_perm:
        lex_perm = part1(lex_perm)
        counter += 1

        if counter == 1000000:
            print(f"{counter:<3} Answer: {''.join([str(i) for i in lex_perm])} in {get_time_running():0.4f} secs")
            break

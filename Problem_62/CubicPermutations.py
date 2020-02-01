from globs import *

"""
    The cube, 41063625 (345**3), can be permuted to produce two other cubes: 56623104 (384**3) and 66430125 (405**3). 
    In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

    Find the smallest cube for which exactly five permutations of its digits are cube.
"""


def get_all_cubes():
    all_cubes = {}
    for k, v in {d: d ** 3 for d in range(1, 10000)}.items():
        s = ''.join(sorted(str(v)))
        if all_cubes.get(s, None):
            all_cubes[s][0] += 1
            all_cubes[s][1].append(v)
            if all_cubes[s][0] == 5:
                break
        else:
            all_cubes[s] = [1, [v]]
    return all_cubes


def main():
    cubes = get_all_cubes()
    m = None
    for k, v in cubes.items():
        if v[0] == 5:
            m = min(v[1])
            break
    return m


if __name__ == '__main__':
    answer = main()
    show_answer(answer)

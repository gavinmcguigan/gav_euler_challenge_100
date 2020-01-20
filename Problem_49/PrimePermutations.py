from globs import *

"""
    The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in 
    two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations 
    of one another.

    There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, 
    but there is one other 4-digit increasing sequence.

    What 12-digit number do you form by concatenating the three terms in this sequence?
"""


def check_for_answers(list_of_primes: list):
    differences = {}
    for n, item in enumerate(list_of_primes[:-1]):
        for next_item in list_of_primes[n+1:]:
            dif = next_item - item
            if differences.get(dif, None):
                differences[dif][0] += 1
                differences[dif][1] += [item, next_item]
            else:
                differences[dif] = [1, [item, next_item]]

    for k, v in differences.items():
        if v[0] > 1 and len(set(v[1])) == 3:
            return sorted(list(set(v[1])))
    else:
        return False


def main():
    """ The idea here, is to first, generate primes of 4 digits, ascending.  Then sort the digits in ascending order,
    before using that as a dictionary key which will hold a list of each prime that has those digits. Then once we
    have that for all primes, we check the lists for primes that are have the same difference. """

    counter, a = {}, ''
    for p in gen_primes(1000, 10000):
        s = sorted(list(str(p)))
        if counter.get("".join(s), None):
            counter["".join(s)].append(p)
        else:
            counter["".join(s)] = [p]

    for n, (k, v) in enumerate(counter.items()):
        if len(v) > 2:
            r = check_for_answers(v)
            if r:
                a = "".join([str(num) for num in r])
                if a != '148748178147':
                    break
    return a


if __name__ == '__main__':
    answer = main()
    show_answer(answer)

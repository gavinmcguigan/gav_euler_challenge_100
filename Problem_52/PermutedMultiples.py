from globs import *

"""
    It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, 
    but in a different order.

    Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""


def check_perms(list_of_perms: list):
    for perm in list_of_perms:
        new_num = int("".join(perm))
        if check_multiples(new_num):
            return new_num
    else:
        return False


def second_answer():
    """ Tried to cut down the amount of values to test.  However, it appears that in doing so,
    it actually takes longer. """
    lists = []
    for i, t in zip(range(5, 7), (100000, 1000000)):
        alist = [i for i in list(permutations('1234567890', i)) if (int("".join(i)) <= t//6 and i[0] != '0')]
        lists.append(alist)

    answer = None
    for l in lists:
        answer = check_perms(l)
        if answer:
            break

    return answer


def check_multiples(new_num: int):
    for m in range(2, 7):
        new_val = m * new_num
        c = sorted(str(new_num)) == sorted(str(new_val))  # Checks if both values have the same digits.
        if not c:
            break
    else:
        return True
    return False


def first_answer():
    """ This was my first brute force answer which seems to get the job done pretty quickly.  """
    answer = None
    for i in range(100000, 1000000):
        if check_multiples(i):
            answer = i
            break

    return answer


def main():
    a = first_answer()
    show_answer(a)

    reset_start_time()
    a = second_answer()
    show_answer(a, val=2)


if __name__ == '__main__':
    main()

from globs import *

"""
    Template
"""


def gen_combos(first=None, middle=None, total=None, remove=None, last=None):

    nums = [i for i in range(1, 11)]
    if remove:
        nums = [i for i in range(1, 11) if i not in remove]

    combo_list = list(permutations(nums, 3))

    for c in combo_list:
        if first:
            if c[0] == first:
                yield c
        else:
            if last:
                if c[1] == middle and sum(c) == total and c[2] == last:
                    yield c
            else:
                if c[1] == middle and sum(c) == total:
                    yield c


def find_numerically_lowest_node(nodes):
    lowest = 10
    first_indx = None
    for n, node in enumerate(nodes):
        if node[0] < lowest:
            lowest = node[0]
            first_indx = n

    a = nodes[first_indx:] + nodes[:first_indx]
    b = "".join(["".join([str(i) for i in t]) for t in a])

    return int(b)


def main():
    greatest = 0
    inc = 0
    for i in range(6, 0, -1):
        for a in gen_combos(first=i):
            for b in gen_combos(middle=a[2], total=sum(a), remove=(a[0],)):
                for c in gen_combos(middle=b[2], total=sum(a), remove=(a[0], b[0], b[1])):
                    for d in gen_combos(middle=c[2], total=sum(a), remove=(a[0], b[0], b[1], c[0], c[1])):
                        for e in gen_combos(middle=d[2], total=sum(a),
                                            remove=(a[0], b[0], b[1], c[0], c[1], d[0], d[1]), last=a[1]):

                            tt = "".join([str(z) for z in a + b + c + d + e])
                            if len(tt) == 16:
                                ordered_intval = find_numerically_lowest_node([a, b, c, d, e])
                                inc += 1
                                # EULER_LOGGER.debug(f"{sum(a):<5} - {inc:<4} a: {str(a):<10}  b: {str(b):<10}  "
                                #                    f"c: {str(c):<10}  d: {str(d):<10}  e:{e}")
                                if ordered_intval > greatest:
                                    greatest = ordered_intval
                                    break

    return greatest


if __name__ == '__main__':
    answer = main()
    show_answer(answer)

from globs import *

"""
    Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in 
    this example), each solution can be described uniquely. For example, the above solution can be described by 
    the set: 4,3,2; 6,2,1; 5,1,3.

    It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in 
    total.
    
    Total	Solution Set
    9	    4,2,3; 5,3,1; 6,1,2
    9	    4,3,2; 6,2,1; 5,1,3
    10	    2,3,5; 4,5,1; 6,1,3
    10	    2,5,3; 6,3,1; 4,1,5
    11	    1,4,6; 3,6,2; 5,2,4
    11	    1,6,4; 5,4,2; 3,2,6
    12	    1,5,6; 2,6,4; 3,4,5
    12	    1,6,5; 3,5,4; 2,4,6
    
    By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 
    432621513.
    
    Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. 
    What is the maximum 16-digit string for a "magic" 5-gon ring?
"""


def gen_combos(first=None, middle=None, total=None, remove=None, last=None):
    """ Generator the returns 3 digit tuples with digits between 1 & 10 depending on params passed in. """

    nums = [i for i in range(1, 11)]
    if remove:
        nums = [i for i in range(1, 11) if i not in remove]

    combo_list = list(permutations(nums, 3))

    for c in combo_list:
        # yields all combinations that start with first
        if first:
            if c[0] == first:
                yield c

        # yields all combinations where the sum of each combo  == total AND the middle digit == middle
        else:
            if last:
                if c[1] == middle and sum(c) == total and c[2] == last:
                    yield c
            else:
                if c[1] == middle and sum(c) == total:
                    yield c


def find_numerically_lowest_node(nodes: tuple) -> int:
    """ Returns an integer after sorting the nodes in order of node with first element being the lowest. """
    lowest = 10
    first_indx = None
    for n, node in enumerate(nodes):
        if node[0] < lowest:
            lowest = node[0]
            first_indx = n

    a = nodes[first_indx:] + nodes[:first_indx]
    b = "".join(["".join([str(i) for i in t]) for t in a])

    return int(b)


def main() -> int:
    greatest = 0
    for i in range(6, 0, -1):
        for a in gen_combos(first=i):
            for b in gen_combos(middle=a[2], total=sum(a), remove=(a[0],)):
                for c in gen_combos(middle=b[2], total=sum(a), remove=(a[0], b[0], b[1])):
                    for d in gen_combos(middle=c[2], total=sum(a), remove=(a[0], b[0], b[1], c[0], c[1])):
                        for e in gen_combos(middle=d[2], total=sum(a),
                                            remove=(a[0], b[0], b[1], c[0], c[1], d[0], d[1]), last=a[1]):

                            tt = "".join([str(z) for z in a + b + c + d + e])
                            if len(tt) == 16:
                                ordered_intval = find_numerically_lowest_node((a, b, c, d, e))
                                if ordered_intval > greatest:
                                    greatest = ordered_intval

    return greatest


if __name__ == '__main__':
    answer = main()
    show_answer(answer)

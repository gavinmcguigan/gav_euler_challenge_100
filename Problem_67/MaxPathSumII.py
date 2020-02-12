from globs import *

"""
    By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total 
    from top to bottom is 23.

            3
           7 4
          2 4 6
         8 5 9 3
    
    That is, 3 + 7 + 4 + 9 = 23.
    
    Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K 
    text file containing a triangle with one-hundred rows.

    NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this 
    problem, as there are 2**99 altogether! If you could check one trillion (1012) routes every second it would take 
    over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)


"""


def remove_last_row(triangle):
    for n, i in enumerate(triangle[-2][:-1]):
        if triangle[-1][n] > triangle[-1][n + 1]:
            triangle[-2][n] += triangle[-1][n]
        else:
            triangle[-2][n] += triangle[-1][n + 1]

    del triangle[-1]

    if len(triangle) > 1:
        return remove_last_row(triangle)
    else:
        return triangle[0][0]


def tri_from_problem_18():
    tri = """
                  75
                 95 64
                17 47 82
               18 35 87 10
              20 04 82 47 65
             19 01 23 75 03 34
            88 02 77 73 07 63 67
           99 65 04 28 06 16 70 92
          41 41 26 56 83 40 80 70 33
         41 48 72 33 47 32 37 16 94 29
        53 71 44 65 25 43 91 52 97 51 14
       70 11 33 28 77 73 17 78 39 68 17 57
      91 71 52 38 17 14 91 43 58 50 27 29 48
     63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
    """
    tri_list = [[int(b) for b in g] for g in [i.split(' ') for i in [i.strip(' ') for i in tri.split('\n')[1:-1]]]]

    EULER_LOGGER.debug(tri_list)
    tri_list = fill_with_zeros(tri_list)

    return remove_last_row(tri_list)


def fill_with_zeros(t: list) -> list:
    """ Makes all rows (lists) be of the same length by adding 0s """
    last_row_len = len(t[-1])
    for row in t:
        while len(row) < last_row_len:
            row.append(0)
    return t


def main():
    """
        Read contents of the file to a list of strings each representing a new row in the triangle.
        Remove line breaks, split each row by a ' ' and convert to a list.
        For each list, fill with 0s until they are all the same size.
        Pass the list of list to the remove_last_row function which returns the largest sum path.

    """
    with open("p067_triangle.txt", "r") as f:
        triangle = f.readlines()

    triangle = [[int(i) for i in group] for group in [row.strip('\n').split(' ') for row in triangle]]
    triangle = fill_with_zeros(triangle)

    return remove_last_row(triangle)


if __name__ == '__main__':
    answer = main()
    show_answer(answer)

"""
    In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

    The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

    What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally)
    in the 20×20 grid?

"""

GRID = """
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
"""


class FourByFour:
    squares_processed = 0
    max_product = 1
    which_square = None

    def __init__(self, square: list):
        FourByFour.squares_processed += 1
        self.square = square
        self.largest_product_of_this_square = 0
        self.this_square = FourByFour.squares_processed

    def calculate_products(self):

        self.calc_horizontals()
        self.calc_verticals()
        self.calc_diagonals()

        if self.largest_product_of_this_square > FourByFour.max_product:
            FourByFour.max_product = self.largest_product_of_this_square
            FourByFour.which_square = self.this_square

        # self.summary()

    def calc_horizontals(self):
        max_hor_prod = 0
        for line in self.square:
            prod = 1
            for element in line:
                prod *= element

            else:
                if prod > max_hor_prod:
                    max_hor_prod = prod

        if max_hor_prod > self.largest_product_of_this_square:
            self.largest_product_of_this_square = max_hor_prod

    def calc_verticals(self):
        prods = [1, 1, 1, 1]
        for line in self.square:
            for n, (p, element) in enumerate(zip(prods, line)):
                prods[n] *= element

        if max(prods) > self.largest_product_of_this_square:
            self.largest_product_of_this_square = max(prods)

    def calc_diagonals(self):
        prods = [1, 1]

        for line in range(0, 4):
            for element in range(0, 4):
                if line == element:
                    prods[0] *= self.square[line][element]

                elif line + element == 3:
                    prods[1] *= self.square[line][element]

        if max(prods) > self.largest_product_of_this_square:
            self.largest_product_of_this_square = max(prods)

    def summary(self):
        print(f"\nSquare {FourByFour.squares_processed:<3}:  Largest Product: {self.largest_product_of_this_square}")
        print(f"{self.square}")


def single_square(l, m, n, o, g):
    top_list = []

    for a in range(l, m):
        nestest_list = []
        for b in range(n, o):
            nestest_list.append(g[a][b])
        top_list.append(nestest_list)

    FourByFour(top_list).calculate_products()


def get_squares(g):
    len_of_row = len(g[0])
    len_of_col = len(g)

    # This gives me a list of "ranges" going from left to right.
    li = [(a, b) for a in range(0, len_of_row + 1) for b in range(0, len_of_col + 1) if b - a == 4]

    # This moves the row down 1 each time, then we go left to right again.
    for i in range(len_of_col - 3):
        for x, y in li:
            single_square(i, i + 4, x, y, g)


if __name__ == '__main__':
    # print(GRID)
    GRID = GRID.__repr__()

    # Beautiful is better than ugly != Simple is better than complex. Hmmmm
    # Creates a list of lists of ints. Each list within the list represents a row.
    grid = [[int(i) for i in sublist] for sublist in [line.split(' ') for line in GRID.split("\\n")[1:-1]]]
    get_squares(grid)

    print(f"\nAnswer: {FourByFour.max_product}")

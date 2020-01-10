from globs import *
from queue import Queue
"""
    Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there
    are exactly 6 routes to the bottom right corner.

    How many such routes are there through a 20×20 grid?

"""


def my_effort(grid_size):
    start = [1, 1]
    next_row = []
    counter = 0

    while counter < grid_size:
        for n, num in enumerate(start):
            if n > 0:
                next_row.append(num + start[n - 1])
            else:
                next_row = [1]

        next_row.append(1)
        start = next_row

        if len(start) % 2:
            counter += 1

    return max(next_row)


if __name__ == '__main__':
    answer = my_effort(grid_size=20)
    print(f"Answer: {answer}")

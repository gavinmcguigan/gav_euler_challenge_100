from globs import *

"""
    Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13
    
    Coloured values from webpage are: 21, 25, 7, 9, 1, 5, 3, 17, 13
    
    It can be verified that the sum of the numbers on the diagonals is 101.
    
    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""


def start():
    total = 1
    for n, i in enumerate(range(3, 1002, 2)):
        total += 4*(i**2) - 6*i + 6

    return total


if __name__ == '__main__':
    answer = start()
    show_answer(answer)

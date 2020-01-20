from globs import *

"""
    The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

    Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
"""


def main():
    s = 0
    for i in range(1, 1001):
        s += pow(i, i)

    return str(s)[-10:]


if __name__ == '__main__':
    answer = main()
    show_answer(answer)

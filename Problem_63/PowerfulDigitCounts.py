from globs import *

"""
    The 5-digit number, 16807=7**5, is also a fifth power. Similarly, the 9-digit number, 134217728=8**9, 
    is a ninth power.
    
    How many n-digit positive integers exist which are also an nth power?
"""


def _gen_numbers(break_point=100):
    n, last_yield = 0, 0
    while True:
        n += 1
        for y in range(1, 25):
            e = n**y
            if len(str(e)) == y:
                yield e, n, y
                last_yield = n
        if n - last_yield > break_point:
            break


def main():
    return len(list(_gen_numbers()))


if __name__ == '__main__':
    answer = main()
    show_answer(answer)

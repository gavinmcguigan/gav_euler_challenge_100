from globs import *

"""
    The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

    Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
    
    (Please note that the palindromic number, in either base, may not include leading zeros.)
    """


def check_if_palindrome(s):
    second_half = s[-1:-len(s)//2: -1] if len(s) % 2 else s[-1:-len(s)//2 - 1: -1]
    if s[:len(s)//2] == second_half:
        return True
    return False


def start():
    total = sum([i for i in range(0, 1000001) if check_if_palindrome(f"{i}") if check_if_palindrome(f"{i:b}")])
    return total


if __name__ == '__main__':
    answer = start()
    show_answer(answer)


from itertools import product

"""
A palindromic number reads the same both ways.  The largest palindrome made from the product of two 2-digit
numbers is 9009 = 91 * 99.

Find the largest palindrome number made from the product of two 3-digit numbers.
"""


def check_if_palindrome(num: str) -> bool:
    first = num[0:len(num)//2]
    second = num[-1:len(num)//2:-1] if len(num) % 2 else num[-1:len(num)//2-1:-1]
    return True if first == second else False


if __name__ == '__main__':
    answer = max([a*b for a in range(999, 99, -1) for b in range(999, 99, -1) if check_if_palindrome(str(a*b))])
    print(answer)


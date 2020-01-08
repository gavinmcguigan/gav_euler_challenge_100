from math import sqrt

"""
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a**2 + b**2 = c**2
    For example, 3**2 + 4**2 = 9 + 16 = 25 = 5*2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.

"""


def pythagoras(a, b):
    c = sqrt(a**2 + b**2)
    if a + b + c == 1000:
        ans = a * b * c
        return ans
    return False


if __name__ == '__main__':
    for i, j in [(a, b) for a in range(500) for b in range(500) if b > a]:
        answer = pythagoras(i, j)
        if answer:
            print(f"Answer: {int(answer)}")
            break

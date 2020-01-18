from globs import *

"""
    The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in 
    some order, but it also has a rather interesting sub-string divisibility property.

    Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
    
    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17
    Find the sum of all 0 to 9 pandigital numbers with this property.
    """


def get_combos_of_10_digits():
    c = permutations('9876543210', 10)        # 3628800  -> 3265920 no leading 0    :  starting with 0: 362880
    for i in c:
        v = "".join(i)
        yield v


def check_sub_string_pans(val: str):

    for x, d in zip(range(7, 0, -1), [17, 13, 11, 7, 5, 3, 2]):
        if int(val[x] + val[x+1] + val[x+2]) % d:
            return False
    return True


def main():
    g = get_combos_of_10_digits()
    sum = 0
    for p in g:
        if check_sub_string_pans(p):
            sum += int(p)
    return sum


if __name__ == '__main__':
    answer = main()
    show_answer(answer)

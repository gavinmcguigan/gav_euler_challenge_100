from globs import *

"""
    Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576
    
    By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated 
    product of 192 and (1,2,3)
    
    The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 
    918273645, which is the concatenated product of 9 and (1,2,3,4,5).
    
    What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an 
    integer with (1,2, ... , n) where n > 1?
    
"""


def is_pandigital(product: str):
    """ Removes each digit found in passed in string, product.  If it manages to remove them all, then
    it's pandigital.
    """

    reference = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    try:
        for letter in product:
            reference.remove(letter)
    except ValueError:
        return False
    else:
        return True


def gen_permutations():
    """ Generator all combinations of 4 digits, 3 digits, 2 digits and 1 digit from the
    list of numbers provided. i.e. Generates 4-digit, 3-digit, 2-digit & 1-digit pandigital numbers.
    """
    for i in range(1, 5):
        a = list(permutations(['9', '8', '7', '6', '5', '4', '3', '2', '1'], i))
        for num in a:
            joined = "".join(num)
            yield joined, int(joined)   # yields as string and int


def main():
    """ Multiply each pandigital number generated by 1, then 2, then 3....etc, adding the resulted string to generated
    pandigital

    Upper limit that satisfies n > 1 would be 9876 as 1x 9876 + 2x 9876 => 9876 + 19998 => 987619998  and the next
    pandigital would be 98765 which would give a result of 98765197530 when n == 2, which is > 9 digits.
    """
    highest_so_far = 0

    g = gen_permutations()
    for s, i in g:
        for j in range(2, 15):
            result = i * j
            s += str(result)
            if len(s) == 9 and is_pandigital(s):
                if int(s) > highest_so_far:
                    highest_so_far = int(s)

    return highest_so_far


if __name__ == '__main__':
    answer = main()
    show_answer(answer)

from globs import *

"""
    An irrational decimal fraction is created by concatenating the positive integers:

    0.123456789101112131415161718192021...
    
    It can be seen that the 12th digit of the fractional part is 1.
    
    If dn represents the nth digit of the fractional part, find the value of the following expression.
    
    d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

answer = 1


def looking_for_dn(current_string, r):
    global answer
    for n in [1, 10, 100, 1000, 10000, 100000, 1000000]:
        if n in range(r[0], r[1]):
            EULER_LOGGER.debug(f"d{n:<10} =>  {current_string[n - 1 - r[0]]}")
            answer *= int(current_string[n - 1 - r[0]])


def main():
    string_slice, total_len = '', 0
    ranges = (0, 0)                         # Keeps track of the ranges the string slice has.

    def reset_string(r, current_str, current_total):
        current_total += len(current_str)
        r = (r[1], r[1] + len(current_str))
        looking_for_dn(current_str, r)
        return "", r, current_total

    for i in range(1, 185186):              # This upper limit ensures the string length is just over 1 million.
        string_slice += str(i)
        if len(string_slice) > 500000:
            string_slice, ranges, total_len = reset_string(ranges, string_slice, total_len)


if __name__ == '__main__':
    main()
    show_answer(answer)

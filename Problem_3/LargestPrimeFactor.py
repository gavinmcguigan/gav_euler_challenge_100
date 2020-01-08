from math import sqrt

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def check_if_prime(num_to_check: int) -> bool:
    top_val = sqrt(num_to_check)
    if not top_val.is_integer():
        top_val = int(top_val)
        if not top_val % 2:
            top_val -= 1

        for n in range(top_val, 1, -2):
            if not num_to_check % n:
                break
        else:
            if num_to_check % 2:
                return True
    return False


def calc_largest_prime_fact(seed: int = 13195) -> int:
    running_num = seed
    factor = 2
    running_total = 1

    while running_total != seed:
        if not running_num % factor:
            running_num //= factor
            running_total *= factor if check_if_prime(factor) else running_total
            print(f'{factor:<10} - {running_total} ')
        else:
            factor = 3 if factor == 2 else factor + 2
    return factor


if __name__ == '__main__':
    f = calc_largest_prime_fact(600851475143)
    print(f"\nAnswer: {f}")


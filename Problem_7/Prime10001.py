from math import sqrt

"""
    By listing the first six prime number: 2, 3, 5, 7, 11 and 13, we can see tha the 6th prime is 13.

    What is the 10001st prime number?

"""
VAL = 10001


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


def count_primes() -> int:
    check_if_this_num_is_prime = 1
    primes_found = 1
    prime10001_not_found = True

    while prime10001_not_found:
        check_if_this_num_is_prime += 2
        found = check_if_prime(check_if_this_num_is_prime)
        if found:
            primes_found += 1
            if primes_found == VAL:
                prime10001_not_found = False

    return check_if_this_num_is_prime


if __name__ == '__main__':
    answer = count_primes()
    print(f"Answer: {answer}")

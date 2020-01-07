"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""
MAX_VAL = 20


def primes_up_to_val(val: int):
    prime_list = []
    for n in range(2, val):
        for a in range(2, n):
            if not n % a and a != n:
                break
        else:
            prime_list.append(n)
    return prime_list


def calc_prime_factors(start_num: int, prime_list) -> list:
    running_num = start_num
    running_total = 1
    prime_fact_list = []
    while running_total != start_num:
        for factor in prime_list:
            if not running_num % factor:
                running_num //= factor
                running_total *= factor
                prime_fact_list.append(factor)
    return prime_fact_list


if __name__ == '__main__':
    occurrence_dict = {k: 0 for k in range(MAX_VAL, 1, -1)}
    prime_l = primes_up_to_val(MAX_VAL)

    for i in range(MAX_VAL, 0, -1):
        list_prime_factors = (calc_prime_factors(i, prime_l))

        for k, v in occurrence_dict.items():
            occurrences = list_prime_factors.count(k)
            if occurrences > occurrence_dict[k]:
                occurrence_dict[k] = occurrences

    total = 1
    for k, v in occurrence_dict.items():
        if v:
            total *= k ** v

    print(f"Answer: {total}")


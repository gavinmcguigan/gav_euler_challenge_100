from globs import *
from multiprocessing import Pool, cpu_count

"""
    Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive 
    numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all 
    less than nine and relatively prime to nine, φ(9)=6.
    
    The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

    Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

    Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
"""


def atask(t, start, stop):
    starttime = get_time_running()
    minimum = 10
    n_val = None
    r_val = None
    for n in range(start, stop):
        r = n
        if not is_prime(n):
            for x in [i for i in gen_get_divisors(n) if is_prime(i)]:
                r *= 1 - 1 / x

        else:
            continue

        if n/r < minimum and sorted(str(int(r))) == sorted(str(n)):
            minimum = n/r
            n_val = n
            r_val = int(r)

        # EULER_LOGGER.debug(f"{n:<10}{int(r):<10} {n/int(r)}")

    return {'Task': t,
            'Start': start,
            'Stop': stop,
            'n': n_val,
            'Totient': r_val,
            'n/totient min': minimum,
            'Duration': f"{get_time_running() - starttime:0.4f}"}


def main():
    results = []
    p = Pool(cpu_count() - 1)
    top_limit = 9000000
    start, stop, task = 2, 100002, 0
    while stop < top_limit:
        task += 1
        r = p.apply_async(atask, args=(task, start, stop))
        results.append(r)

        start, stop = stop, stop + stop - start

    minimum = 10
    n_val = None
    for each in results:
        result = each.get()
        if result['n/totient min'] < minimum:
            minimum = result['n/totient min']
            n_val = result['n']

        EULER_LOGGER.debug(f"{result}")

    return minimum, n_val


if __name__ == '__main__':
    answer = main()
    show_answer(answer)

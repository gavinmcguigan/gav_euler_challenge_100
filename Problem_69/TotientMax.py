from globs import *
from multiprocessing import Pool, cpu_count

"""
    Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers 
    less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and 
    relatively prime to nine, φ(9)=6.

    n	Relatively Prime	φ(n)	n/φ(n)
    2	1	                1	    2
    3	1,2	                2	    1.5
    4	1,3	                2	    2
    5	1,2,3,4	            4	    1.25
    6	1,5	                2	    3
    7	1,2,3,4,5,6	        6	    1.1666...
    8	1,3,5,7	            4	    2
    9	1,2,4,5,7,8	        6	    1.5
    10	1,3,7,9	            4	    2.5
    
    It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.
    
    Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
"""


def totient_task(t, start, stop):
    starttime = get_time_running()
    maximum = 0
    n_val, r_val = None, None

    for n in range(start, stop):
        r = 1
        if not is_prime(n):
            for x in [i for i in gen_get_divisors(n) if is_prime(i)]:
                r *= 1 - 1 / x
            s = 1 / r
        else:
            s = n / (n - 1)

        if s > maximum:
            maximum = s
            n_val = n
            r_val = int(s)

    return {'Task': t,
            'Start': start,
            'Stop': stop,
            'n': n_val,
            'Totient': r_val,
            'n/totient max': maximum,
            'Duration': f"{get_time_running() - starttime:0.4f}"}


def main():
    p = Pool(cpu_count() - 1)
    start, stop, task, top_limit, results = 2, 50000, 0, 1000000, []
    while True:
        task += 1
        r = p.apply_async(totient_task, args=(task, start, stop))
        results.append(r)
        if stop > top_limit:
            break

        start, stop = stop, stop + stop - start
        if stop > top_limit:
            stop = top_limit + 1

    maximum = 0
    n_val = None
    for each in results:
        result = each.get()
        if result['n/totient max'] > maximum:
            maximum = result['n/totient max']
            n_val = result['n']

        EULER_LOGGER.debug(f"{result}")

    return maximum, n_val


if __name__ == '__main__':
    answer = main()
    show_answer(answer)

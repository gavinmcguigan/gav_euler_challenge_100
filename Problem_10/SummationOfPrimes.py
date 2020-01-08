from math import sqrt
from multiprocessing import Process, Queue
from globs import *

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17

Find the sum of all the primes below two million?

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


def task(q, max_min, task_num):
    starttime = get_time_running()
    q.put(sum([i for i in range(*max_min, -2) if check_if_prime(i)]))
    print(f"Task {task_num} took {get_time_running() - starttime: 0.4} secs")


def multiprocess_method():
    result_q = Queue()
    procs = []
    # for n, ints in enumerate([(1999999, 1599999), (1599999, 1199999), (1199999, 799999), (799999, 2)]):
    for n, ints in enumerate([(1999999, 1299999), (1299999, 2)]):
        p = Process(target=task, args=(result_q, ints, n))
        p.start()
        procs.append(p)

    for p in procs:
        p.join()

    answer = 2
    while result_q.qsize():
        answer += result_q.get(block=False)

    print(f"\nAnswer: {answer} in {get_time_running():0.4f} secs")


def single_process_method():
    sum_of_primes = sum([i for i in range(1999999, 2, -2) if check_if_prime(i)]) + 2
    print(f"\nAnswer: {sum_of_primes} in {get_time_running():0.4f} secs")


if __name__ == '__main__':
    # single_process_method()
    multiprocess_method()

    # 142913828922
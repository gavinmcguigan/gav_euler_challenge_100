from time import sleep
from multiprocessing import Process, Queue
from globs import *
"""
    The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has
    not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def calc_chain_size(seed: int) -> int:
    chain_size, seq = 1, seed
    while seq != 1:
        seq = seq//2 if not seq % 2 else (seq * 3) + 1
        chain_size += 1
    return chain_size


def generate_seed(low_high, que=None, t=0):
    largest_chain, seed = 0, 0
    for n in range(*low_high):
        chain = calc_chain_size(n)
        if chain > largest_chain:
            largest_chain = chain
            seed = n

    if que is not None:
        que.put((seed, largest_chain))
    else:
        return seed, largest_chain


def multiprocess_method() -> (int, int):
    result_q = Queue()
    procs = []
    for t, ints in enumerate([(1, 500000), (500000, 1000000)]):
        p = Process(target=generate_seed, args=(ints, result_q, t))
        p.start()
        procs.append(p)

    for p in procs:
        p.join()

    answer, l_chain = 0, 0
    while result_q.qsize():
        a, b = result_q.get(block=False)
        if b > l_chain:
            answer, l_chain = a, b

    return answer, l_chain


if __name__ == '__main__':
    # ans, longest_chain = generate_seed((500000, 1000000))
    ans, longest_chain = multiprocess_method()
    print(f'Answer: {ans}   ->  Chain Size: {longest_chain}')

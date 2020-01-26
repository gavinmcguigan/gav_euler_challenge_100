from time import perf_counter
from logging import StreamHandler, Formatter, DEBUG, INFO, getLogger
from math import sqrt
from itertools import permutations, combinations_with_replacement, combinations

APP_START_TIME = perf_counter()


def get_time_running():
    return perf_counter() - APP_START_TIME


def reset_start_time():
    global APP_START_TIME
    APP_START_TIME = perf_counter()


# Logger -------------------------------------------------------------------------------------------------------------
class LogHandler(StreamHandler):
    def __init__(self):
        StreamHandler.__init__(self)
        formatter = Formatter('%(asctime)s.%(msecs)03d:%(levelname)-8s%(lineno)-4d: %(message)s',)
        formatter.datefmt = '%H:%M:%S'
        self.setFormatter(formatter)
        self.setLevel(DEBUG)


EULER_LOGGER = getLogger(__name__)
log_handler = LogHandler()
EULER_LOGGER.addHandler(log_handler)
EULER_LOGGER.setLevel(DEBUG)


# Functions ----------------------------------------------------------------------------------------------------------
def is_prime(num_to_check: int):
    if num_to_check in [2]:
        return True

    if not num_to_check % 2 or num_to_check < 0:
        return False

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


def show_answer(answer, val: int = 1):
    EULER_LOGGER.info(f"Answer {val} -> '{answer}' in {get_time_running():0.4f} secs.")


def get_factorial(n: int) -> int:
    fact = 1
    for f in range(1, n + 1):
        fact *= f

    return fact


# Generators ---------------------------------------------------------------------------------------------------------
def gen_get_divisors(seed):
    """ Yields in order of largest -> smallest divisors of number passed in. """
    already_yielded = []
    yield_despues = []
    for n in range(1, int(sqrt(seed))):
        if not seed % n:
            result = seed // n
            if result not in already_yielded:
                yield_despues.append(n)

            if result != n:
                yield result
                already_yielded.append(result)

    for n in reversed(yield_despues):
        yield n


def gen_primes(start=1, end=100):
    if not start % 2:
        start -= 1

    if start == 0:
        start = 1

    if start == 1:
        yield 1
        start = 2

    if start == 2:
        yield 2
        start = 3

    if start < end:
        for i in range(start, end + 1, 2):
            if is_prime(i):
                yield i
    else:
        if not start % 2:
            start += 1

        for i in range(start, end, -2):
            if is_prime(i):
                yield i


def gen_factorials(low_limit=1, high_limit=10):
    """ Calculates factorials between low limit and high limit and stores them in a
        dictionary for quicker look-up.  Alternate would be to store them in a dictionary.

        You can send in a value that's not yet been calculated and the it  will start from
        the highest value that it already has stored, in order to keep it efficient.

    """
    factorials_found = {0: 1}
    f = None

    def looper(low, high, start_val):
        f = start_val
        for i in range(low, high):
            f *= i
            factorials_found[i] = f             # Adds all products to dict whilst looking for target.

        return f

    looper(low_limit, high_limit, 1)

    while True:
        recd_this = (yield f)
        f = factorials_found.get(recd_this, None)
        if f is None:
            max_key = max(factorials_found)
            max_value_we_already_have = factorials_found.get(max_key, None)
            f = looper(low=max_key + 1, high=recd_this + 1, start_val=max_value_we_already_have)


if __name__ == '__main__':
    pass

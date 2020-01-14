from time import perf_counter
from logging import StreamHandler, Formatter, DEBUG, INFO, getLogger
from math import sqrt

APP_START_TIME = perf_counter()


def get_time_running():
    return perf_counter() - APP_START_TIME


# Logger -------------------------------------------------------------------------------------------------------------
class LogHandler(StreamHandler):
    def __init__(self):
        StreamHandler.__init__(self)
        formatter = Formatter('%(asctime)s.%(msecs)03d:%(levelname)-8s%(module)-18s%(lineno)-4d: %(message)s',)
        formatter.datefmt = '%H:%M:%S'
        self.setFormatter(formatter)
        self.setLevel(DEBUG)


EULER_LOGGER = getLogger(__name__)
log_handler = LogHandler()
EULER_LOGGER.addHandler(log_handler)
EULER_LOGGER.setLevel(DEBUG)


# Functions ----------------------------------------------------------------------------------------------------------
def is_prime(num_to_check: int):
    if num_to_check < 0:
        return False

    if num_to_check == 2:
        return True

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


def show_answer(answer):
    EULER_LOGGER.info(f"Answer -> '{answer}' in {get_time_running():0.4f} secs.")

# Generators ---------------------------------------------------------------------------------------------------------

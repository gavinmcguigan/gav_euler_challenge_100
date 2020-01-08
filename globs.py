from time import perf_counter


APP_START_TIME = perf_counter()


def get_time_running():
    return perf_counter() - APP_START_TIME

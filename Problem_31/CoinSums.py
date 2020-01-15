from globs import *

"""
    In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in 
    general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
    It is possible to make £2 in the following way:
    
    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
    How many different ways can £2 be made using any number of coins?
"""


def eulerdotnet_answer() -> int:
    def ways(target: int, avc: int) -> int:
        if avc <= 1:
            return 1

        res = 0
        while target >= 0:
            res += ways(target, avc - 1)
            target -= coins[avc - 1]

        return res

    return ways(200, len(coins))


def calc_combos(coins_left: int, remaining: int) -> int:
    if remaining == 0:  # If remaining is 0 , we have a solution, +1.
        return 1

    if remaining < 0 or (coins_left <= 0 and remaining >= 1):
        return 0

    return calc_combos(coins_left - 1, remaining) + calc_combos(coins_left, remaining - coins[coins_left - 1])


if __name__ == '__main__':
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    answer = eulerdotnet_answer()
    # answer = calc_combos(len(coins), 200)
    show_answer(answer)
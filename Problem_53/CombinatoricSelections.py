from globs import *

"""
    There are exactly ten ways of selecting three from five, 12345:

    123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
    
    In combinatorics, we use the notation, (5/3)=10.
    
    In general, (nr)=n!r!(n−r)!, where r≤n, n!=n×(n−1)×...×3×2×1, and 0!=1.
    
    It is not until n=23, that a value exceeds one-million: (2310)=1144066.
    
    How many, not necessarily distinct, values of (nr) for 1≤n≤100, are greater than one-million?
"""


def gen_facts():
    n, facts = None, {0: 1}
    for i in range(1, 101):
        facts[i] = get_factorial(i)

    while True:
        recd = (yield n)
        n = facts.get(recd, None)


def using_formula(g, n: int):
    counter = 0
    nf = g.send(n)
    for r in range(n, 0, -1):
        rf = g.send(r)
        nrf = g.send((n - r))
        if (nf/nrf)/rf > 1000000:
            counter += 1

    return counter


def main():
    g = gen_facts()
    g.send(None)
    a = 0
    for n in range(1, 101):
        a += using_formula(g, n)
    return a


if __name__ == '__main__':
    answer = main()
    show_answer(answer)

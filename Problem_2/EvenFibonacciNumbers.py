"""
Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous two terms.  By starting with 1 and 2,
 the first 10 terms will be
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89 ....

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of
the even-valued terms.

"""


def fib_feeder():
    alist = []
    a, b = 1, 1
    keep_going = True
    while keep_going:
        a, b = b, a + b

        if a <= 4000000:
            if not a % 2:
                alist.append(a)
        else:
            keep_going = False

    print(alist)
    return sum(alist)


def main():
    answer = fib_feeder()
    print(answer)


if __name__ == '__main__':
    main()
"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

"""


def get_sum_of_factorial():
    product = 1
    for i in range(1, 101):
        product *= i

    sum = 0
    for num in str(product):
        sum += int(num)

    return sum


if __name__ == '__main__':
    answer = get_sum_of_factorial()
    print(f'Answer: {answer}')

"""
Problem 1
If we list all the natural numbers below 10 tha tare multiples of 3 or 5, we get 3, 5, 6, and 9. The
sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

answer = sum([n for n in range(1, 1000) if not n % 3 or not n % 5])
print(answer)

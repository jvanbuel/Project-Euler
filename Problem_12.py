import numpy as np
import functools as fnc

# Triangle number: m = n(n+1)/2
# The clue of this problem: you don't need to iterate over all numbers to find divisors.
# Iteration until sqrt(n) is enough, since it is the maximal divisor (sqrt(n)*sqrt(n) = n).
# Warning: // (integer division) is implemented only since Python 3!


def triangle_number(num):
    return num*(num+1)/2


def no_divisors(n):
    return set(fnc.reduce(list.__add__, ([i, n // i] for i in range(1, int(np.sqrt(n)) + 1) if n % i == 0)))



triangle_next = 1
no_div = 0

while no_div <= 500:
    triangle_num = triangle_number(triangle_next)
    no_div = len(no_divisors(triangle_num))
    print(no_div)
    triangle_next += 1

print(triangle_num)



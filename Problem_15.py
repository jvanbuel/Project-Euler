import numpy as np

# Simple mathematical problem: to find number of routes, one just has to take a combination of 20 out of 40
# Reason: you need in total 20 steps down, and 20 steps to the right. The order can be arbitrary (ergo, combination).


def combination(n, m):
    return np.math.factorial(m)/(np.math.factorial(m-n)*np.math.factorial(n))

Ans = combination(20, 40)
print(int(Ans))

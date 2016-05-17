import numpy as np


base = 2
exponent = 1000
length = int(np.ceil(exponent*np.log10(2)))  # 2^1000 = 10^(log(2)*1000) and 10^n has n digits (or ceil(n) if n not integer)
number = np.zeros(length)
number[0] = 2
exp_index = 1

while exp_index < exponent:
    exp_index += 1
    carry_over = 0
    for i in range(0, length):
        new = base * number[i] + carry_over
        number[i] = new % 10
        carry_over = new // 10

Sum = 0
for i in range(0, length):
    Sum += number[i]

print(Sum)

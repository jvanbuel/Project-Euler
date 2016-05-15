from math import gcd

# Use greatest common divisor (gcd) from math module to
# calculate least common multiple (lcm) of x and y: lcm = x*y/gcd(x,y)


def lcm(x, y):
    return int(x*y/gcd(x, y))

current_lcm = 20

for i in range(19, 2, -1):
    current_lcm = lcm(i, current_lcm)

print(current_lcm)

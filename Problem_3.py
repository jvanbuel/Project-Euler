import numpy as np

# Brute force by loading in primes.txt, containing prime numbers.
# Primes were also found by brute force (see is_prime.py).
# Could also just use some files you can find online. Could have used
# Sieve of Atkin, but too lazy to implement.

f = open("primes.txt", "r")
primes = f.readlines()
for x in range(0, len(primes)):
    primes[x] = int(primes[x].rstrip())

Limit = 600851475143
Found = False
max_prime_div = 2

while not Found:
    for num in primes:
        if Limit % num == 0:
            max_prime_div = num
            Limit /= num
            if Limit == 1:
                Found = True

print(max_prime_div)

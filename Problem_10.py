# Now used Eratosthenes' sieve to find prime numbers below 2e6
# since much faster than is_prime.py

f = open("Eratosthenes_primes.txt", "r")
primes = f.readlines()
for p in range(0, len(primes)):
    primes[p] = int(primes[p].lstrip())

print(sum(primes))

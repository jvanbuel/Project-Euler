f = open("primes.txt", "r")
primes = f.readlines()
for x in range(0, len(primes)):
    primes[x] = int(primes[x].rstrip())

index = 10001
print(primes[index-1])

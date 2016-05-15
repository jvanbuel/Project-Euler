import numpy as np

# Open "primes.txt" file, check if number is already in there;
# if not, add prime to list

# mrange can be used for very long arrays (otherwise memory problems are possible)


def mrange(start, stop, step):
    while start < stop:
        yield start
        start += step


def is_prime(num):
    f = open("primes.txt", "r")
    numbers = f.readlines()
    f.close()
    for x in range(0, len(numbers)):
        numbers[x] = int(numbers[x].rstrip())
    numbers = set(numbers)
    if num in numbers:
        return True
    elif num == 2:
        f = open("primes.txt", "a")
        f.write(str(2)+"\n")
        f.close()
        return True
    elif (num < 2) or (num % 2 == 0):
        return False
    else:
        check = all(num % i for i in mrange(3, int(np.sqrt(num)) + 1, 2))
        if check:
            f = open("primes.txt", "a")
            f.write(str(num) + "\n")
            f.close()
        return check

for l in range(1, 400000):
    print(is_prime(l))

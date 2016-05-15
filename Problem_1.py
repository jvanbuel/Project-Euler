

# Brute force
Maxint = 1000
Sum = 0
for x in range(3, Maxint):
    if x % 3 == 0 or x % 5 == 0:
        Sum += x

Ans = "Sum = %d" % Sum
print(Ans)



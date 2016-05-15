
# Brute force

a = 1
b = 1
Sum = 0

limit = 4E6
while b <= limit:
    buff = a + b
    a = b
    b = buff
    print(b)
    if b % 2 == 0:
        Sum += b

Ans = "The sum equals %d" % Sum
print(Ans)
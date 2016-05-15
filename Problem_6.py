# To compute the difference between (a**2 + b**2 + c**2 + ...)
# and (a + b + c + ...)**2, one only needs to calculate 2*(ab + bc + ac + ...),
# i.e. all possible unique combinations of two numbers out of (a,b,c,...)


Sum = 0

for x in range(1, 100):
    for y in range(x+1, 101):
        s = "%d*%d" % (x, y)
        Sum += 2*x*y


print(Sum)
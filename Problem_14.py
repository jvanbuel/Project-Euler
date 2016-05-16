# This is again brute force... More elegantly: if n is even, then it's chain length is just 1 more than that of n/2

def collatz(n):
    if n % 2 == 0:
        return int(n/2)
    else:
        return int(3*n + 1)


def chain_length(number, length):
    if number != 1:
        return chain_length(collatz(number), length+1)
    elif number == 1:
        return length + 1

max = int(1e6)
max_chain = 0
buff_chain = 0

for i in range(1, max):
    buff_chain = chain_length(i,0)
    if buff_chain > max_chain:
        max_chain = buff_chain
        print("number" + str(i) + ", max chain_length "+str(max_chain))

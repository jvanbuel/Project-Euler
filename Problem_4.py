# Define a function is_palindrome to check whether a given
# number is palindromic. Start from x*y with (x,y) = (999, 999) and go down incrementally
#  to find palindrome


def is_palindrome(num):
    buffer = num
    reverse_num = 0
    while buffer > 0:
        dig = buffer % 10
        reverse_num = reverse_num*10 + dig
        buffer = (buffer-dig)/10
    if num == reverse_num:
        return True
    else:
        return False

max_palindrome = 0

for x in range(999, 100, -1):
    for y in range(999, 100, -1):
        if (is_palindrome(x*y)) & (x*y > max_palindrome):
            max_palindrome = x*y

print(max_palindrome)
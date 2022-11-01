# https://www.codewars.com/kata/577b9960df78c19bca00007e

def find_digit(num, nth):
    if nth <= 0:
        return -1
    if nth > len(str(num)):
        return 0
    else:
        return int(reverse(num)[nth-1])
    
def reverse(x):
    return str(x)[::-1]
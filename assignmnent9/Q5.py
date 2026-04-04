# Write a program to find factorial using recursion.

def factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return -1
    elif n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
n = int(input('Enter factorial number:'))
res = factorial(n)
print(res)
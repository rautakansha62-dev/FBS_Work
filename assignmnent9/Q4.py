# Write a program to find sum of n numbers using recursion.

def sumofNum(n):
    if n > 0:
        return n +  sumofNum(n-1)
    elif n == 0:
        return 0
    else:
        return None
    
n = int(input('Enter number to find:'))
res = sumofNum(n)
print(res)
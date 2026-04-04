# Write a program to find sum of following series using recursive functions:
#i. 1! + 2! + 3! + 4! +..... + n!
# Note : For fact and sum two recursive functions

def sumofSeries(n):
    if n > 0:
        return n +  sumofSeries(n - 1)
    elif (n == 0):
        return 0
    else:
        return None
    
n = 5
res = sumofSeries(n)
print(res)
    
# Write a program to reverse a given number using recursive function.

def reverse(n, rev=0):
    if n < 0:
        return None
    elif n == 0:
        return rev
    else:
        rev = rev * 10 + n % 10
        return reverse(n // 10, rev)
    
n = int(input('Enter reverse number:'))
res = reverse(n)
print(res)
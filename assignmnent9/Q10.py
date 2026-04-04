# Write a program to reverse a number using recursion.

def reverse(n, rev = 0):
    if n < 0:
        return None
    elif n == 0:
        return rev
    else:
        rev = rev * 10 + n % 10
        return reverse(n // 10, rev)
    
n = int(input('Enter reverse number:'))
rev = reverse(n)
print(rev)
# WAP to check pallindrone number using recursion.

def isPallindrome(n, rev = 0):
    if n < 0:
        return None
    elif n == 0:
        return rev
    else:
        rev = rev * 10 + n % 10
        return isPallindrome(n // 10, rev)
    
n = int(input('Enter number to check pallindrome or not:'))
rev = isPallindrome(n)
if rev == n:
    print('is Pallindrome')


# Write a program to check if given number is Armstrong or not using recursive
# function.

def armstrong(n):
    if n < 0:
        return None
    elif n == 0:
        return 0
    else:
        return (n % 10) ** 3 + armstrong(n // 10)
    
    
num = int(input('enter number to check armstrong or not:'))
res = armstrong(num)
print(res)

    
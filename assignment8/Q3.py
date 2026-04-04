# Write a program to find sum of following series using functions :
#a. 1+ 2 + 3 + 4+..... + n

def sumOfseries(n):
    total = 0
    for i in range(1,n+1):
        total += i
        
    return total

num = int(input('Enter number:'))
ans = sumOfseries(num)

print(f'The sum of series 1+ 2 + 3 + 4+.....+ n for n {num} is {ans}')
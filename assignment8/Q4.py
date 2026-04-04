#Sum of all odd numbers between 1 to n

def sumOfoddNos(n):
    sum = 0
    for i in range(1,n+1):
        if(i % 2 != 0):
            sum += 0
    return sum

num = int(input('Enter number:'))
ans = sumOfoddNos(num)

print(f'The sum of odd numbers between 1 to n {num} is {ans}')
    
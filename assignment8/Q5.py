# Sum of all prime numbers between 1 to n

def SumOfprimeno(n):
    sum = 0
    for i in range(2, n+1):
        for j in range(2, i):
            if(i % j == 0):
                break
        else:
            sum += 0
            
    return sum
num = int(input('Enter a number:'))
ans = SumOfprimeno(num)

print(f'The sum of all prime no between 1 to n {num} is {ans}')        
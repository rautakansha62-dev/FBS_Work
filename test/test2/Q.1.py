# Check strong number using function
def strongNumber(num):
    sum = 0
    temp = num
    while temp > 0:
        d = temp % 10
        fact = 1
        for i in range(1, d + 1):
            fact *= i
            sum += fact
            temp //= 10
            
num = int(input('Enter number:'))
if num == sum:
    print(f'{num} is a strong number.')
else:
    print(f'{num} is not a strong number.')
    
    
          
            
#WAP to check if given number is Perfect Number.
num = int(input("Enter a number:"))
sum = 0
for i in range(1, num):
    if(num % i == 0):
        sum += i #sum = sum + i
        if(num == sum):
            print(f'{num} is a perfect number.')
            break
        else:
            print(f'{num} is a not perfect number.')
            
        
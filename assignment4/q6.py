#WAP to check if a given number is prime number or not.
num = int(input('Enter a number to check prime or not:'))
for i in range(1, num):
    if(num % i == 0):
        print(f'{num}is not a prime number.')
        break
else:
    print(f'{num}is prime number.')
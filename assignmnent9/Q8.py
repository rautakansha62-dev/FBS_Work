# Write a program to check whether a number is prime or not using recursion.

def isPrime(n, i=2):
    for num in range(2, n):
        for i in range(2, num):
            if(num % i == 0):
                return False
            return True
        
n = int(input('Enter number to check prime or not:'))
res = isPrime(n)
if res == True:
    print(f'{n} is a prime number.')
else:
    print(f'{n} is not a prime number.')
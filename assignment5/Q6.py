#Write a program to print first n prime numbers.
num = 6
for i in range(2, num):
    if(num% i == 0):
        print(f'{num} is not a prime num.')
    else:
        print(f'{num} is a prime num.')
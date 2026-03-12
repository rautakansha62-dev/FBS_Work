#Write a program to print prime numbers between 1 to 100.
n = int(input("Enter number till prime number you want to print:"))
for num in range(2,n):
    for i in range(2, num):
        if(num % i == 0):
            #print(f'{num} id not a prime number. ')
            break
        else:
            #print(f'{num} is a prime number.')
            print(num)

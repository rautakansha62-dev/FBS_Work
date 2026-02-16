#Write a program to check if given 3 digit number is a palindrome or not.
num = int(input('Enter 3 digit number to check pallindrome or not: '))
temp = num
rev_num = 0

while(temp > 0):
    d = temp % 10
    temp = temp // 10
    rev_num = rev_num * 10 + d
    if(num == rev_num):
        print(f'{num} id a pallindrone number.')
    else:
        print(f'{num} is not a pallindrone number.')
# Write a program to check if entered number is a palindrome or not.

def palindrome(num):
    temp = num
    rev_num = 0
    while(temp > 0):
        d = temp % 10
        temp = temp // 10
        rev_num = rev_num * 10 + d
        
    if(num == rev_num):
       print(f'a palindrone number.')
    else:
        print(f'not a palindrome number.')

num = int(input('Enter number:'))
ans = palindrome(num) 

print(f'{num} is {ans}')
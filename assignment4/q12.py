#Write a program to check if given number is Armstrong number or not.
#(Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
#4*4*4*4)
num = int(input('Enter a number to check armstrong or not:'))
temp = num
sum = 0
while(temp > 0):
    d = temp % 10
    temp = temp // 10 # temp //= 10
    sum += d ** 3 
    if(num == sum):
        print(f'{num} is a armstrong number.')
    else:
        print(f'{num} is not a armstrong number.')
#Find the sum of three-digit number.
num=int(input('enter a three digit num:'))
a=num%10
b=num//10
c=b%10
d=b//10
sum=a+c+d
print(f'sum of three digit num is:{sum}')

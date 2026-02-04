#Write a program to reverse three-digit number.
num=int(input('enter three digit num:'))
a=num%10
b=num//10
c=b%10
d=b//10
rev_num=a*100+c*10+d
print(f'reverse of three digit num is:{rev_num}')

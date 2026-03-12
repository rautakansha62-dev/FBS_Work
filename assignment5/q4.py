#WAP to print Armstrong number within a given range
num = int(input('enter number:'))
temp = num
while(temp > 0):
    d = temp % 10
    print(d)
    temp = temp // 10 #temp //= 10

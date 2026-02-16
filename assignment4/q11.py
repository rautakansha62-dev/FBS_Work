#WAP to check if given number Strong Number.
num = int(input("Enter number:"))
temp = num
sum = 0
while(temp>0):
    d = temp % 10
    temp = temp //10 #temp //= 10
    fact = 1
    for i in range(1, d+1):
        fact *= i #fact = fact *i
        sum += fact
        if(num == sum):
            print(f'{num} is a strong number.')
        else:
            print(f'{num} is not a strong number.')
    
#Write a program find reverse of a number

def reversenos(n):
    temp = 0
    
    while (temp > 0):
        d = temp % 0
        temp = temp // 10
        n = (n * 10) + d
    
    return n

num = int(input('Enter number:'))
ans = reversenos(num)

print(f'reverse no of {num} is {ans}')
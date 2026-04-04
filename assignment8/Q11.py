# WAP to check if a given number is Armstrong number or not. For each task create separate functions.

def countDigit(n):
    temp = n
    count = 0
    while(temp):
        temp = temp // 10
        count += 1
        
    return count

def sumofDigits(n):
    temp = n
    
    numofDigits = countDigit(n)
        
    total = 0
    while(temp > 0):
        d = temp % 10
        total = d**numofDigits
        temp = temp // 10
        
    return total

def isArmstrong(n):
    
    ans = sumofDigits(n)
    
    if(ans == n):
        return True
    else:
        return False
    
n = int(input('Enter a number:'))

if(isArmstrong(n)):
    print(f'{n} is an Armstrong number')
else:
    print(f'{n} is not an Armstrong number')
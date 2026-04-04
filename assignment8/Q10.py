# Write a program to check if entered year is a leap year or not.

def CheckLeapYear(n):
    if(n % 4 == 0):
        if(n % 100 == 0):
            if(n % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
year = int(input('Enter number:'))
isLeapYear = CheckLeapYear(year)

if(isLeapYear):
    print(f'{year} is Leap year.')
else:
    print(f'{year}is not yeap year.')
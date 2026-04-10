#WAP to print following pattern

def printZ():
    for i in range(1, 11):
        for j in range(1, 11):
            if i == 1 or i == 10:
                print('*', end=' ')
            elif j == 11-i:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
            
printZ()
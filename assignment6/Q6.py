for i in range(1, 6):
    num = 1
    for j in range(1, 6 - i): 
        print(' ',end = ' ')
        
    for j in range(1, 2*i):
        print(num, end= ' ')
        num += 1
        
    print()
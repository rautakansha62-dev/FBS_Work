n = 5
for i in range(1, n + 1):
    print(' '*(n - i), end='')
    for j in range(1, i + 1):
        if  j == 1 or j == i:
            print(j, end=' ')
        elif i < n:
            print(' ',end=' ')
        else:
            print(j, end=' ')
    print()
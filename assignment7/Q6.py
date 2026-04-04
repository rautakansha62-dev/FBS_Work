for i in range(1, 6):
    for j in range(1, 6):
        if i == 1 or j == 1 or (i + j == 6):
            print(f'{i if j==1 else (j if i==1 else 5)}', end=' ')
        else:
            print(' ', end=' ')
    print()
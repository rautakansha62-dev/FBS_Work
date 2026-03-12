n=int(input('enter:'))
for i in range(1, n+1):
    for s in range(1,n+1-i):
        print(' ',end='')
        num=1
    for j in range(1,i+1):
              print(num,end=' ')
              num=num*(i-j)//j
    print()
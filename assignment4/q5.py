#WAP to print Fibonacci series upto n.
n = int(input("Enter number:"))
a = -1
b = 1
for i in range(n):  #range (5) - 0,1,2,3,4
    c = a + b
    print(c, end = '')
    a=b
    b=c
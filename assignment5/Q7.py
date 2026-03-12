#Write a program to solve the following series :
#a. 1! + 2! + 3! + 4! + .....n!
#b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
#c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
#d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
#e. x - x2/3 + x3/5 - x4/7 + .... to n terms
def sum_factorials(n):
    total = 0
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        total += fact
    return total
def sum_powers(N):
    total = 0
    for i in range(1, N + 1):
        total += N**i
    return total
def geometric_sum(n):
    total = 0
    for i in range(n):
        total += 2**i
    return total
def sum_fraction_series(a):
    total = 0
    for i in range(1, 11):
        total += (a**i) / i
    return total
def alternating_series(x, n):
    total = 0
    for i in range(1, n + 1):
        term = (x**i) / (2*i - 1)
        if i % 2 == 0:
            total -= term
        else:
            total += term
    return total

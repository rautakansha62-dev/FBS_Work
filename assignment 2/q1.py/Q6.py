#WAP to calculate total salary of employee based on basic, da=10% of basic,
#ta=12% of basic, hra=15% of basic. 
basicSal=float(input('enter the basic Sal ='))
da=basicSal*0.1
ta=basicSal*0.12
hra=basicSal*0.15
totalSal=basicSal+da+ta+hra
print(f'total salary of employee is={totalSal}.Rs')
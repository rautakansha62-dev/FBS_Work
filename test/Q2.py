#WAP to calculate simple interest based on principle, Rate and Time (SI = p*r*t/100)
principle = float(input('enter amount:'))
rate = float(input('enter interest:'))
time = float(input('enter years:'))
simple_interest = (principle*rate*time)/100
print('simple interest is:', simple_interest)

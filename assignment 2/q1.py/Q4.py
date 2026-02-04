#WAP to calculate area of triangle and rectangle.

#three sides of tringle x,y,z
#two sides of rectangle l,b

x=float(input("enter first side="))
y=float(input("enter second side="))
z=float(input("enter third side="))
s=(x+y+z)/2
area_tri=(s*(s-x)*(s-y)*(s-z))**0.5
print(f'area of the tringle={area_tri}.')

#two side of rectangle l,b
l=float(input("enter length of rect="))
b=float(input("enterr breadth of rect="))
area = l*b
print(f'area of the rectangle={area}.')



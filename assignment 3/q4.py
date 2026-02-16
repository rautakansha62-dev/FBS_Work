#Write a program to input all sides of a triangle and check whether triangle is valid or
#not.
side1 = float(input('enter side 1:'))
side2 = float(input('enter side 2:'))
side3 = float(input('enter side 3:'))
if (side1 + side2 > side3) and (side2 + side3 > side1) and (side1 + side3 > side2):
    print('valid triangle')
else:
    print('invalid tringle')
    
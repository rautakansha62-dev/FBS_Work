#WAP to input angles of a triangle and check whether triangle is valid or not.
angle1 = float(input('enter angle 1:'))
angle2 = float(input('enter angle 2:'))
angle3 = float(input('enter angle 3:'))
sum_of_angles = angle1 + angle2 + angle3
if sum_of_angles == 180:
    print('valid tringle')
else:
    print('invalid tringle')



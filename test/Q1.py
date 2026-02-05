#WAP to find the area and perimeter of following figure(Accept the length,breadth and radius from user)
import math
len = float(input('enter length:'))
brea = float(input('enter breadth:'))
rad = float(input('enter radius:'))
area_rect = len * brea
perim_rect = 2 * (len + brea)
area_circle = math.pi * rad * rad
circum_circle = 2 *math.pi * rad
print('area of rectangle:', area_rect)
print('perimeter of rect:',perim_rect)
print('area of circle:', area_circle)
print('circumference of circle:', circum_circle)

#Write a program to check if person is eligible to marry or not (male age >=21 and
#female age>=18)
gender = int(input('Enter gender (M/F):')) #F,f,female,Female
age = int(input('Enter age:'))
#if gender == 'F':
if gender in ['F', 'f', 'female', 'Female']:
       if age>18:
           print('Eligible for marriage.')
       else:
           print('pahile padhai to kar le.')
 else:
           if age>21:
               print('Eligible for marriage.')
           else:
               print('bada to ho ja.')
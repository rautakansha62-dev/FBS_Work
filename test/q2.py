#WAP to accept 3 digit number . if first digit is double of second digit and half of third digit then
#display "yes, you have done it", otherwise display "please try next time"
num = int(input('Enter a 3 digit number:'))
first_digit = num //100
second_digit = (num // 10)%10
third_digit = num % 10
if (first_digit == 2 * second_digit) and (third_digit == 2 * first_digit):
    print(f'yes, you have done it')
else:
    print(f'plese try next time')
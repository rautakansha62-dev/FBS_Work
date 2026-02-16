#Write a program to prompt user to enter userid and password. After verifying
#userid and password display a 4 digit random number and ask user to enter the
#same. If user enters the same number then show him success message otherwise
#failed. (Something like captcha)
user_id = input('enter the user id=')
password = input('enter the password=')
if user_id == 'admin' and password == 'admin123':
    import random 
    random_num = random.radiant(1000,2000)
    print(random_num)
    user_id = int(input('enter the number:'))
    if user_id == random_num:
        print("succesful id",success)
    else:
        print("failed is",fail)

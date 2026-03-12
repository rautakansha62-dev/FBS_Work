#Write a program to prompt user to enter userid and password. If Id and
#password is incorrect give him chance to re-enter the credentials. Let him try 3
#times. After that program to terminate.
for attempt in range(3):
    user_id = input('enter user ID:')
    password= input('enter user pass:')
    
    correct_id ='admin'
    correct_password = '1234'
    
    if user_id == correct_id and password == correct_password:
        print('Login successful')
        break
    else:
        remaining_attempts = 2 - attempt
        if remaining_attempts > 0:
            print(f'executed.')
        else:
            print(f'Incorrect.')
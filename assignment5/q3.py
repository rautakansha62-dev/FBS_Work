#Accept no. of passengers from user and per ticket cost. Then accept age of each
#passenger and then calculate total amount to ticket to travel for all of them based on
#following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.
num_passangers = int(input('enter the passenger:'))
ticket_cost= float(input('enter the per ticket:'))

total_amount = 0

for i in range(num_passangers):
    age= int(input(f'enter the age of passenger{i+1}:'))
    
    if age < 12:
        total_amount += ticket_cost * 0.70
    elif age > 59:
        total_amount += ticket_cost * 0.50
    else:
        total_amount += ticket_cost
print(f'The total amount to be paid for {num_passangers} passengers is: {total_amount:.2f}')
#Accept age of five people and also per person ticket amount and then calculate total
#amount to ticket to travel for all of them based on following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.
total_amount = 0
for i in range(5):  #range(5) - 0,1,2,3,4
    age = int(input("enter age:"))
    ticket_amount = int(input("enter ticket amount:"))
    if age < 12:
        total_amount += ticket_amount * 0.7
    elif age >59:
        total_amount += ticket_amount * 0.5
    else:
        total_amount += ticket_amount
        print(f"total amount to pay: {total_amount}")
        
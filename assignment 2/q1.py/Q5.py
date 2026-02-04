#WAP to calculste selling price of book based on cost price and discount.
costprice=float(input('enter the cost price of book:'))
discount=float(input('enter the discount perc:'))
sellingprice=costprice-(costprice*discount/100)
print(f'selling price of book is:{sellingprice}.Rs')

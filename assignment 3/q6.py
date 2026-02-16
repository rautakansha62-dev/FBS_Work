#Write a program to calculate profit or loss.
Cost_price = float(input("Enter the cost price:"))
selling_price = float(input("Enter the selling price:"))
if selling_price > cost_price:
    profit = selling_price - cost_price
    print(f'profit is {profit}')
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print(f'loss is {loss}')

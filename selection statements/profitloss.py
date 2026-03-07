#program to calculate profit or loss
#input of cost price from user
cost_price=float(input("Enter cost price (in Rs): "))
#validating cost price
if cost_price<=0:
    exit("Error: Cost price should be greater than 0")
#input of selling price from user
selling_price=float(input("Enter selling price (in Rs): ")) 
#validating selling price
if selling_price<=0:
    exit("Error: Selling price should be greater than 0")
#Displaying data
print("---------------------------------")
print("Cost Price : Rs ",cost_price)
print("Selling Price : Rs ",selling_price)
#Calculating profit or loss
if selling_price>cost_price:
    print("Profit : Rs ",selling_price-cost_price)
elif selling_price<cost_price:
    print("Loss : Rs ",cost_price-selling_price)
else:
    print("No profit, no loss.")
'''Output:
Enter cost price (in Rs): 5000
Enter selling price (in Rs): 6000
---------------------------------   
Cost Price : Rs  5000.0
Selling Price : Rs  6000.0
Profit : Rs  1000.0
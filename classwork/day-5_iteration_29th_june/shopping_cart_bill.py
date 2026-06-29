'''---------- Shopping Cart Billing System --------

Calculate total bill amount for multiple products.

---------------------------------------------------'''

#--------------------------------------------------
#---------------- Coding --------------------------

n = int(input("Enter Number of Products : "))

total_bill = 0
highest_cost = -1
lowest_cost = 999999

expensive_product = ""
cheap_product = ""

for i in range(n):

    name = input("Enter Product Name : ")
    quantity = int(input("Enter Quantity : "))
    price = float(input("Enter Price per Unit : "))

    cost = quantity * price

    print("Cost of",name,":",cost)

    total_bill += cost

    if(cost > highest_cost):
        highest_cost = cost
        expensive_product = name

    if(cost < lowest_cost):
        lowest_cost = cost
        cheap_product = name

average = total_bill/n

print("Total Bill Amount :",total_bill)
print("Most Expensive Product :",expensive_product)
print("Cheapest Product :",cheap_product)
print("Average Product Cost :",average)

#--------------------------------------------------
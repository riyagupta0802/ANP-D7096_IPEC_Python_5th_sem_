''' -------Inventory Management-------

Problem Statement: 
Create a dictionary to maintain the stock of products in a shop. 
------------------------------------------------
Example: 
{ 
'Laptop': 15, 
'Mouse': 40, 
'Keyboard': 25, 
'Monitor': 10 
} 
-----------------------------------
Implement the following: 

• Add a new product.  
• Update the stock of an existing product.  
• Remove a product from inventory.  
{ 
'Rahul': {'Math': 85, 'Science': 90, 'English': 88}, 
• Display products having stock less than 20.  
• Display the total number of items available in the inventory. '''


# initialize dictionary
inventory = {}

# input details of 4 products
for i in range(4):
    product = input("Enter Product Name: ")
    stock = int(input("Enter Stock: "))
    inventory[product] = stock
print("-------------------------------------------------")

# display inventory
print("Inventory:", inventory)
print("-------------------------------------------------")

# add new product
product = input("Enter New Product Name: ")
stock = int(input("Enter Stock: "))
inventory[product] = stock

print("After Adding Product:", inventory)
print("-------------------------------------------------")

# update stock
product = input("Enter Product Name to Update: ")
if product in inventory:
    stock = int(input("Enter New Stock: "))
    inventory[product] = stock
    print("Stock Updated")
else:
    print("Product not found")
print("-------------------------------------------------")

# remove product
product = input("Enter Product Name to Remove: ")
if product in inventory:
    del inventory[product]
    print("Product Removed")
else:
    print("Product not found")

print("Updated Inventory:", inventory)
print("-------------------------------------------------")

# display products having stock less than 20
print("Products having stock less than 20:")
for product in inventory:
    if inventory[product] < 20:
        print(product, inventory[product])
print("-------------------------------------------------")

# display total stock
total = 0
for product in inventory:
    total = total + inventory[product]

print("Total Items in Inventory =", total)


'''Output:
Enter Product Name: Laptop
Enter Stock: 15
Enter Product Name: Mouse
Enter Stock: 40
Enter Product Name: Keyboard
Enter Stock: 25
Enter Product Name: Monitor
Enter Stock: 10
-------------------------------------------------
Inventory:
{
'Laptop': 15,
'Mouse': 40,
'Keyboard': 25,
'Monitor': 10
}
-------------------------------------------------
Enter New Product Name: Printer
Enter Stock: 18
After Adding Product:
{
'Laptop': 15,
'Mouse': 40,
'Keyboard': 25,
'Monitor': 10,
'Printer': 18
}
-------------------------------------------------
Enter Product Name to Update: Mouse
Enter New Stock: 50
Stock Updated
-------------------------------------------------
Enter Product Name to Remove: Keyboard
Product Removed
Updated Inventory:
{
'Laptop': 15,
'Mouse': 50,
'Monitor': 10,
'Printer': 18
}
-------------------------------------------------
Products having stock less than 20:
Laptop 15
Monitor 10
Printer 18
-------------------------------------------------
Total Items in Inventory = 93'''
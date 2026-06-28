'''---------- Smart Electricity Billing System ----------------

Calculate electricity bill using:

Units          Rate
0 - 100        ₹5/unit
101 - 300      ₹7/unit
Above 300      ₹10/unit

Additional Rules:
• Commercial consumers pay 20% extra.
• Bills above ₹5000 attract 5% surcharge.
• Senior citizens receive 10% discount.

---------------------------------------------------------------
Sample Input
Units Consumed : 450
Consumer Type (Residential/Commercial) : Commercial
Senior Citizen (Y/N) : Y
---------------------------------------------------------------
Sample Output
Base Bill : ₹4500
Commercial Charge : ₹900
Surcharge : ₹270
Senior Citizen Discount : ₹567
Final Bill Amount : ₹5103
---------------------------------------------------------------'''
#--------------------------------------------------------------
#---------------- Coding --------------------------------------

units = int(input("Enter Units Consumed : "))
consumer = input("Enter Consumer Type (Residential/Commercial) : ")
senior = input("Enter Senior Citizen (Y/N) : ")

if(units < 0):
    exit("Invalid Input")

# Base Bill Calculation
if(units <= 100):
    base_bill = units * 5
elif(units <= 300):
    base_bill = units * 7
else:
    base_bill = units * 10

# Commercial Charge Calculation
if(consumer == "Commercial" or consumer == "commercial"):
    commercial_charge = base_bill * 0.20
elif(consumer == "Residential" or consumer == "residential"):
    commercial_charge = 0
else:
    exit("Invalid Consumer Type")

total_bill = base_bill + commercial_charge

# Surcharge Calculation
if(total_bill > 5000):
    surcharge = total_bill * 0.05
else:
    surcharge = 0

total_bill = total_bill + surcharge

# Senior Citizen Discount
if(senior == 'Y' or senior == 'y'):
    discount = total_bill * 0.10
elif(senior == 'N' or senior == 'n'):
    discount = 0
else:
    exit("Invalid Input")

final_bill = total_bill - discount

print("Base Bill : ₹", base_bill)
print("Commercial Charge : ₹", commercial_charge)
print("Surcharge : ₹", surcharge)
print("Senior Citizen Discount : ₹", discount)
print("Final Bill Amount : ₹", final_bill)

#--------------------------------------------------------------

''' Output :
Enter Units Consumed : 450
Enter Consumer Type (Residential/Commercial) : Commercial
Enter Senior Citizen (Y/N) : Y

Base Bill : ₹ 4500
Commercial Charge : ₹ 900.0
Surcharge : ₹ 270.0
Senior Citizen Discount : ₹ 567.0
Final Bill Amount : ₹ 5103.0
'''
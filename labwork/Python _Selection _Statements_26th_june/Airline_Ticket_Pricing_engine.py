'''---------- Airline Ticket Pricing Engine ----------------
An airline calculates ticket fare using:

Base Fare = ₹5000

Additional Charges:
• Business Class -> +₹3000
• Window Seat -> +₹500
• Weekend Travel -> +₹1000

Discounts:
• Age below 12 -> 50%
• Age above 60 -> 20%

Calculate the final ticket fare.
-----------------------------------------------------------
Sample Input
Enter Passenger Age : 65
Business Class(Y/N) : Y
Window Seat(Y/N) : Y
Weekend Travel(Y/N) : Y
-----------------------------------------------------------
Sample Output
Base Fare : ₹5000
Additional Charges : ₹4500
Senior Citizen Discount : 20%
Final Ticket Fare : ₹7600.0
-----------------------------------------------------------'''
#----------------------------------------------------------
#---------------- Coding ----------------------------------

age = int(input("Enter Passenger Age : "))
business = input("Business Class(Y/N) : ").upper()
window = input("Window Seat(Y/N) : ").upper()
weekend = input("Weekend Travel(Y/N) : ").upper()

if(age <= 0):
    exit("Invalid Age")

base = 5000
extra = 0

if(business == "Y"):
    extra += 3000

if(window == "Y"):
    extra += 500

if(weekend == "Y"):
    extra += 1000

fare = base + extra

print("Base Fare : ₹", base)
print("Additional Charges : ₹", extra)

if(age < 12):
    print("Child Discount : 50%")
    fare = fare - (fare * 0.50)
elif(age > 60):
    print("Senior Citizen Discount : 20%")
    fare = fare - (fare * 0.20)

print("Final Ticket Fare : ₹", fare)

#----------------------------------------------------------

''' Output :
Enter Passenger Age : 65
Business Class(Y/N) : Y
Window Seat(Y/N) : Y
Weekend Travel(Y/N) : Y

Base Fare : ₹ 5000
Additional Charges : ₹ 4500
Senior Citizen Discount : 20%
Final Ticket Fare : ₹ 7600.0
'''
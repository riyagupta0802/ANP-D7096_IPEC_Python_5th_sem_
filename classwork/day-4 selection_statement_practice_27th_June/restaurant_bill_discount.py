'''---------- Restaurant Bill Discount ------------------------

Discount Rules:
• Bill below ₹1000 → No Discount
• ₹1000 - ₹2999 → 10% Discount
• ₹3000 or more → 20% Discount

---

Sample Input
Bill Amount : 3200
------------------

Sample Output
20% Discount Applied
---------------------------------------------------------------'''

bill = float(input("Enter Total Bill Amount : "))

if(bill < 1000):
print("No Discount")
elif(bill < 3000):
print("10% Discount Applied")
else:
print("20% Discount Applied")

'''
Output :
Enter Total Bill Amount : 3200

20% Discount Applied
'''

#--------------------------------------------------------------

'''---------- Exam Hall Entry --------------------------------

Students can enter only if they have admit card.

1 → Admit Card Available
0 → Admit Card Not Available

---

Sample Input
Admit Card : 1
--------------

Sample Output
Enter Examination Hall
---------------------------------------------------------------'''

admit_card = int(input("Enter Admit Card Status (1/0) : "))

if(admit_card == 1):
print("Enter Examination Hall")

'''
Output :
Enter Admit Card Status (1/0) : 1

Enter Examination Hall
'''

#--------------------------------------------------------------

'''---------- ATM Cash Withdrawal -----------------------------

Customer can withdraw only if amount is less than or
equal to available balance.

---

Sample Input
Balance : 5000
Withdrawal Amount : 4500
------------------------

Sample Output
Transaction Successful
---------------------------------------------------------------'''

balance = float(input("Enter Account Balance : "))
withdraw = float(input("Enter Withdrawal Amount : "))

if(withdraw <= balance):
print("Transaction Successful")
else:
print("Insufficient Balance")

'''
Output :
Enter Account Balance : 5000
Enter Withdrawal Amount : 4500

Transaction Successful
'''

#--------------------------------------------------------------

'''---------- Internet Speed Rating ---------------------------

Speed Categories:
• Less than 25 Mbps → Slow
• 25 - 99 Mbps → Good
• 100 Mbps or above → Excellent

---

Sample Input
Speed : 120
-----------

Sample Output
Excellent Connection
---------------------------------------------------------------'''

speed = float(input("Enter Internet Speed (Mbps) : "))

if(speed < 25):
print("Slow Connection")
elif(speed < 100):
print("Good Connection")
else:
print("Excellent Connection")

'''
Output :
Enter Internet Speed (Mbps) : 120

Excellent Connection
'''

#--------------------------------------------------------------

'''---------- Electricity Consumption Category ---------------

Consumption Categories:
• Up to 100 Units → Low Consumption
• 101 - 300 Units → Moderate Consumption
• Above 300 Units → High Consumption

---

Sample Input
Units : 245
-----------

Sample Output
Moderate Consumption
---------------------------------------------------------------'''

units = int(input("Enter Electricity Consumption Units : "))

if(units <= 100):
print("Low Consumption")
elif(units <= 300):
print("Moderate Consumption")
else:
print("High Consumption")

'''
Output :
Enter Electricity Consumption Units : 245

Moderate Consumption
'''

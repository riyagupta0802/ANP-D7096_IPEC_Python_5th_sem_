'''---------- Courier Delivery Charge -------------------------

Delivery Charges:
• Weight up to 2 kg → ₹50
• Weight greater than 2 kg and up to 5 kg → ₹100
• Weight greater than 5 kg → ₹180

---------------------------------------------------------------
Sample Input
Weight : 4
---------------------------------------------------------------
Sample Output
Delivery Charge = ₹100
---------------------------------------------------------------'''
#--------------------------------------------------------------
#---------------- Coding --------------------------------------

weight = float(input("Enter Package Weight (kg) : "))

if(weight <= 2):
    print("Delivery Charge = ₹50")
elif(weight <= 5):
    print("Delivery Charge = ₹100")
else:
    print("Delivery Charge = ₹180")

#--------------------------------------------------------------

''' Output :
Enter Package Weight (kg) : 4

Delivery Charge = ₹100
'''
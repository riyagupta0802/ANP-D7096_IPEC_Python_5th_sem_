'''---------- Electricity Consumption Category ----------------

Consumption Categories:
• Up to 100 Units → Low Consumption
• 101–300 Units → Moderate Consumption
• Above 300 Units → High Consumption

---------------------------------------------------------------
Sample Input
Units : 245
---------------------------------------------------------------
Sample Output
Moderate Consumption
---------------------------------------------------------------'''
#--------------------------------------------------------------
#---------------- Coding --------------------------------------

units = int(input("Enter Electricity Consumption Units : "))

if(units <= 100):
    print("Low Consumption")
elif(units <= 300):
    print("Moderate Consumption")
else:
    print("High Consumption")

#--------------------------------------------------------------

''' Output :
Enter Electricity Consumption Units : 245

Moderate Consumption
'''
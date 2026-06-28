'''---------- Mobile Battery Warning --------------------------

Display warning only when battery percentage falls below 15%.

---------------------------------------------------------------
Sample Input
Battery Percentage : 10
---------------------------------------------------------------
Sample Output
Connect Charger Immediately
---------------------------------------------------------------'''
#--------------------------------------------------------------
#---------------- Coding --------------------------------------

battery = int(input("Enter Battery Percentage : "))

if(battery < 15):
    print("Connect Charger Immediately")

#--------------------------------------------------------------

''' Output :
Enter Battery Percentage : 10

Connect Charger Immediately
'''
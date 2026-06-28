'''---------- Multi-Level Access Control System ---------------

Assign access levels based on:

Roles:
• Admin
• Manager
• Employee
• Guest

Conditions:
• Admin + Security Clearance ≥ 5 → Full Access
• Manager + Experience > 5 Years → Department Access
• Employee + Experience > 2 Years → Limited Access
• Guest → Read-Only Access
• Inactive Account → No Access

---------------------------------------------------------------
Sample Input
Role : Admin
Security Clearance : 6
Experience : 0
Account Status : Active
---------------------------------------------------------------
Sample Output
Access Level : FULL ACCESS
---------------------------------------------------------------'''
#--------------------------------------------------------------
#---------------- Coding --------------------------------------

role = input("Enter Role : ")
clearance = int(input("Enter Security Clearance : "))
experience = int(input("Enter Experience (Years) : "))
status = input("Enter Account Status (Active/Inactive) : ")

if(clearance < 0 or experience < 0):
    exit("Invalid Input")

if(status == "Inactive" or status == "inactive"):
    print("Access Level : NO ACCESS")

elif(role == "Admin" or role == "admin"):
    if(clearance >= 5):
        print("Access Level : FULL ACCESS")
    else:
        print("Access Level : NO ACCESS")

elif(role == "Manager" or role == "manager"):
    if(experience > 5):
        print("Access Level : DEPARTMENT ACCESS")
    else:
        print("Access Level : NO ACCESS")

elif(role == "Employee" or role == "employee"):
    if(experience > 2):
        print("Access Level : LIMITED ACCESS")
    else:
        print("Access Level : NO ACCESS")

elif(role == "Guest" or role == "guest"):
    print("Access Level : READ-ONLY ACCESS")

else:
    print("Invalid Role")

#--------------------------------------------------------------

''' Output :
Enter Role : Admin
Enter Security Clearance : 6
Enter Experience (Years) : 0
Enter Account Status (Active/Inactive) : Active

Access Level : FULL ACCESS
'''
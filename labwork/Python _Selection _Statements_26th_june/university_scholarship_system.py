'''---------- University Scholarship System -------------------

Scholarship is awarded based on percentage:

Percentage      Scholarship
95+             100%
90 - 94         75%
85 - 89         50%
80 - 84         25%
Below 80        No Scholarship

Conditions:
• Family income must be below ₹8,00,000.
• Students with disciplinary actions receive no scholarship.

---------------------------------------------------------------
Sample Input
Percentage : 92
Family Income : 500000
Disciplinary Action (Y/N) : N
---------------------------------------------------------------
Sample Output
Scholarship Awarded : 75%
---------------------------------------------------------------'''
#--------------------------------------------------------------
#---------------- Coding --------------------------------------

percentage = float(input("Enter Percentage : "))
income = float(input("Enter Family Income : "))
disciplinary = input("Enter Disciplinary Action (Y/N) : ")

if(percentage < 0 or percentage > 100 or income < 0):
    exit("Invalid Input")

if(income >= 800000 or disciplinary == 'Y' or disciplinary == 'y'):
    print("Scholarship Awarded : No Scholarship")
else:
    if(percentage >= 95):
        print("Scholarship Awarded : 100%")
    elif(percentage >= 90):
        print("Scholarship Awarded : 75%")
    elif(percentage >= 85):
        print("Scholarship Awarded : 50%")
    elif(percentage >= 80):
        print("Scholarship Awarded : 25%")
    else:
        print("Scholarship Awarded : No Scholarship")

#--------------------------------------------------------------

''' Output :
Enter Percentage : 92
Enter Family Income : 500000
Enter Disciplinary Action (Y/N) : N

Scholarship Awarded : 75%
'''
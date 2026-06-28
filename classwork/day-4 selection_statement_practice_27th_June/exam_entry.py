'''---------- Exam Hall Entry --------------------------------

Students can enter the examination hall only if they
are carrying their admit card.

1 → Admit Card Available
0 → Admit Card Not Available

---------------------------------------------------------------
Sample Input
Admit Card : 1
---------------------------------------------------------------
Sample Output
Enter Examination Hall
---------------------------------------------------------------'''
#--------------------------------------------------------------
#---------------- Coding --------------------------------------

admit_card = int(input("Enter Admit Card Status (1/0) : "))

if(admit_card == 1):
    print("Enter Examination Hall")

#--------------------------------------------------------------

''' Output :
Enter Admit Card Status (1/0) : 1

Enter Examination Hall
'''a
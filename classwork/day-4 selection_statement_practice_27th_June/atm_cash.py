'''---------- ATM Cash Withdrawal -----------------------------

Customer can withdraw money only if requested amount
does not exceed available balance.

---------------------------------------------------------------
Sample Input
Balance : 5000
Withdrawal Amount : 4500
---------------------------------------------------------------
Sample Output
Transaction Successful
---------------------------------------------------------------'''
#--------------------------------------------------------------
#---------------- Coding --------------------------------------

balance = float(input("Enter Account Balance : "))
withdraw = float(input("Enter Withdrawal Amount : "))

if(withdraw <= balance):
    print("Transaction Successful")
else:
    print("Insufficient Balance")

#--------------------------------------------------------------

''' Output :
Enter Account Balance : 5000
Enter Withdrawal Amount : 4500

Transaction Successful
'''
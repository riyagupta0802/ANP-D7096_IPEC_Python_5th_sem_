'''to calculate the remaining bank account balance after withdrawal'''

# input of current balance from user
current_balance = float(input("Enter the current balance: "))

# input of withdrawal amount from user
withdrawal_amount = float(input("Enter the withdrawal amount: "))

# calculation of remaining balance
print("Remaining Balance is: ", current_balance - withdrawal_amount)
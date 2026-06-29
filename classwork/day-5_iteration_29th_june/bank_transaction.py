'''---------- Bank Transaction Summary ------------

Enter fixed number of transactions.

---------------------------------------------------'''

#--------------------------------------------------
#---------------- Coding --------------------------

n = int(input("Enter Number of Transactions : "))

deposit = 0
withdrawal = 0
balance = 0

for i in range(n):

    amount = float(input("Enter Transaction Amount : "))

    if(amount > 0):
        deposit += amount
    else:
        withdrawal += abs(amount)

    balance += amount

print("Total Deposit :", deposit)
print("Total Withdrawal :", withdrawal)
print("Final Balance :", balance)

#--------------------------------------------------
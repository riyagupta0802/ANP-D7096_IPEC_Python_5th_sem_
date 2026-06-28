'''---------- Secure Vault Access -----------------------------

A digital vault can only be opened if the user enters
the correct security code.

Condition:
• Security Code = 7890 → Access Granted

---

Sample Input
Security Code : 7890
--------------------

Sample Output
Access Granted to the Vault.
---------------------------------------------------------------'''

code = int(input("Enter Security Code : "))

if(code == 7890):
print("Access Granted to the Vault.")

#---------------------------
'''
Output :
Enter Security Code : 7890

Access Granted to the Vault.
'''

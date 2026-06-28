'''---------- Cybersecurity Login Validation ------------------

A login system validates:
• Username
• Password
• OTP

Conditions:
• All correct → Login Successful
• Incorrect OTP → Re-enter OTP
• Incorrect Password after 3 attempts → Account Locked
• Incorrect Username → User Not Found

---------------------------------------------------------------
Sample Input
Username : admin
Password : admin123
OTP : 4567
---------------------------------------------------------------
Sample Output
Login Successful
Welcome Admin
---------------------------------------------------------------'''
#--------------------------------------------------------------
#---------------- Coding --------------------------------------

username = input("Enter Username : ")
password = input("Enter Password : ")
otp = input("Enter OTP : ")

if(username != "admin"):
    print("User Not Found")

elif(password != "admin123"):
    print("Account Locked")

elif(otp != "4567"):
    print("Re-enter OTP")

else:
    print("Login Successful")
    print("Welcome Admin")

#--------------------------------------------------------------

''' Output :
Enter Username : admin
Enter Password : admin123
Enter OTP : 4567

Login Successful
Welcome Admin
'''
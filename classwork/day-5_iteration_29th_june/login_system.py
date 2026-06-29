'''---------- Login System ------------------------

Maximum Login Attempts = 3

Username : admin
Password : python123

---------------------------------------------------'''

#--------------------------------------------------
#---------------- Coding --------------------------

for i in range(1,4):

    print("Attempt",i)

    username = input("Username : ")
    password = input("Password : ")

    if(username == "admin" and password == "python123"):
        print("Login Successful")
        break
    else:
        print("Invalid Credentials")
else:
    print("Account Locked")

#--------------------------------------------------
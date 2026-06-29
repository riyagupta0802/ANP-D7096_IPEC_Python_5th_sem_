'''---------- Password Strength Checker -----------

Password must contain at least 8 characters.

User gets 3 attempts.

---------------------------------------------------'''

#--------------------------------------------------
#---------------- Coding --------------------------

for i in range(1, 4):

    password = input("Enter Password : ")

    if(len(password) >= 8):
        print("Password Accepted.")
        break
    else:
        print("Password too short.")

#--------------------------------------------------
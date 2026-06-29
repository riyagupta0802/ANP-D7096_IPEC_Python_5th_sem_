'''---------- ATM PIN Verification ----------------

The correct PIN is 4589.

User gets 3 attempts to enter the correct PIN.

---------------------------------------------------'''

#--------------------------------------------------
#---------------- Coding --------------------------

correct_pin = 4589

for i in range(1, 4):

    pin = int(input("Enter PIN : "))

    if(pin == correct_pin):
        print("Access Granted")
        break
    else:
        print("Incorrect PIN")

#--------------------------------------------------
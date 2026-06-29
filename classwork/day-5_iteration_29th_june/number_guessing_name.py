'''---------- Number Guessing Game ----------------

Secret Number = 37

User gets 5 attempts.

---------------------------------------------------'''

#--------------------------------------------------
#---------------- Coding --------------------------

secret = 37

for i in range(1, 6):

    guess = int(input("Guess the Number : "))

    if(guess == secret):
        print("Correct Guess")
        break
    elif(guess > secret):
        print("Too High")
    else:
        print("Too Low")

#--------------------------------------------------
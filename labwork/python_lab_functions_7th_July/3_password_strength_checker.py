'''------------- Password Strength Checker----------------

Problem statement:
Write a function check_password(password) that checks whether a password is strong. 
A password is considered Strong if: 
• It contains at least 8 characters.  
• It contains at least one uppercase letter.
• It contains at least one lowercase letter.  
• It contains at least one digit.  
The function should return: 
• "Strong Password" or  
• "Weak Password"  
The main program should accept a password from the user and display the result.  '''


#fuction to check password strength
def check_password(password):
    lower = False
    upper = False
    digit = False

    for x in password:
        if x.isupper():
            upper = True
        if x.islower():
            lower = True
        if x.isdigit():
            digit = True

    if len(password) >= 8 and upper == True and lower == True and digit == True:
        return "Strong Password"
    else:
        return "Weak Password"

# main program
password = input("Enter your password: ")
print(check_password(password))

'''
Output:
Enter your password: Riya@120
Strong Password'''
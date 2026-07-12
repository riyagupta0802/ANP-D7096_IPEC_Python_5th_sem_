''' ---Password Validator---
Write a Python program that repeatedly asks the user to enter a password until it satisfies all the 
following conditions: 
• Minimum length should be 8 characters.  
• Must contain at least one uppercase letter.  
• Must contain at least one lowercase letter.  
• Must contain at least one digit.  
Use a while loop for repeated input and a user-defined function to validate the password. 
Display "Password Accepted" once the password is valid. 
-------------------------------------------------------------------------------------------
Sample Input 
abc 
password 
Password 
Password123 
Sample Output 
Invalid Password 
Invalid Password 
Invalid Password 
Password Accepted 
    • statements  
    • break
'''

# Function to check password
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
        return True
    else:
        return False


# Main program
while True:
    password = input("Enter Password: ")

    if check_password(password):
        print("Password Accepted")
        break
    else:
        print("Invalid Password")

'''Output:

Enter Password: abc
Invalid Password
Enter Password: password
Invalid Password
Enter Password: Password
Invalid Password
Enter Password: Password123
Password Accepted
'''
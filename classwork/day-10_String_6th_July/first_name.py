'''Wap to ask the user to input their full name and display the first name from it without using lib functions'''

#input of full name
name = input("Enter your full name :")
#initialize first name variable
first_name =""
for x in name:
    if(x==" "):
        break
    #increment first name variable
    first_name=first_name + x
#-----------------------------------------------------
print("Your first name is :" , first_name)


'''
Output:-

Enter your full name :Riya Gupta
Your first name is : Riya
'''
'''Wap to calculate simple interest using Function'''

def calculate_simple_interest(principal,rate,time):
    return(principal*rate*time)/100   #
#--------------------------------------------------
#main program
principal=float(input("Enter the principal (in rs):"))
rate=float(input("Enter the rate of interest (in %):"))
time=int(input("Enter time (in year):"))
print("Simple interest : Rs", calculate_simple_interest(principal,rate,time))

'''Output:
'''
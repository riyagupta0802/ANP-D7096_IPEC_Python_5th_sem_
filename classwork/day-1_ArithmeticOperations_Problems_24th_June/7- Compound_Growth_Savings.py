'''to calculate the final amount of savings assuming it doubles every year'''

# input of initial amount from user
initial_amount = float(input("Enter the initial amount: "))

# input of number of years from user
number_of_years = int(input("Enter the number of years: "))

# calculation of final amount
print("Final Amount is: ", initial_amount * (2 ** number_of_years))
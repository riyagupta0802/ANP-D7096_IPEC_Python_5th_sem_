'''to calculate the total recharge amount based on the data pack selected'''

# input of cost per GB from user
cost_per_gb = float(input("Enter the cost per GB: "))

# input of number of GBs from user
number_of_gbs = float(input("Enter the number of GBs: "))

# calculation of total recharge cost
print("Total Recharge Cost is: ", cost_per_gb * number_of_gbs)
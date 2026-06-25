'''to calculate the remaining pizza slices after equal distribution among children'''

# input of total pizza slices from user
total_pizza_slices = int(input("Enter the total number of pizza slices: "))

# input of number of children from user
number_of_children = int(input("Enter the number of children: "))

# calculation of remaining slices
print("Remaining Slices are: ", total_pizza_slices % number_of_children)
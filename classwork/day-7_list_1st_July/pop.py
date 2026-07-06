# Creating a list with elements
lst = [1, 2, 3, 4, 5, 5, 42]

# Deleting the last item from the list using pop() method

# Case-1
lst.pop()

# Print the list after pop
print(lst)

# Output
# [1, 2, 3, 4, 5, 5]


# Case-2
position = int(input("Enter the position to remove: "))

# Remove the element at the given position
lst.pop(position - 1)

# Print the updated list
print(lst)
'''Program to input 10 numbers from the user and ask the user for a position to remove an element from the list'''

# Creating a blank list
numbers = []

print("Enter any 10 numbers:")

# Taking input from the user
for i in range(10):
    num = int(input())
    # Adding the number to the list
    numbers.append(num)

print("-------------------------")

# Displaying the original list
print("Original List:", numbers)

# Taking the position from the user
position = int(input("Enter the position of number to be removed: "))

# Checking whether the position is valid
if position >= -len(numbers) and position < len(numbers):
    
    # Removing the element from the given position
    removed = numbers.pop(position)

    # Displaying the removed element
    print("Removed Element:", removed)

    # Displaying the updated list
    print("Updated List:", numbers)

else:
    print("Invalid Position")
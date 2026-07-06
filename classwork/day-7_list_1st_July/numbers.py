'''Write a Python program to input 20 numbers from the user and store them in a list.
 Ask the user to enter a number whose duplicate occurrences are to be removed.
   If the number appears more than once, remove all duplicate occurrences while keeping 
   only one occurrence in the list. Otherwise, display "No duplication found.
   " Finally, display the updated list.'''


# Creating a blank list
numbers = []

print("Enter any 20 numbers:")
for i in range(5):
    # Input element from the user
    num = int(input())

    # Inserting data into the list
    numbers.append(num)

# Displaying the original list
print("-------------------")
print("Original list :", numbers)

# Element to be removed from the list
num = int(input("Enter the number whose duplicates you want to remove: "))

#To find frequency ofthe number in the list
c = numbers.count(num)
if(c==0):
    print("element not found")
elif(c==1):
    print("No duplication found.")
else:
    numbers.remove(num)
    # Remove duplicate occurrences, keeping one copy
    for i in range(c - 1):
        numbers.remove(num)

    print("Updated list after removing duplicates :", numbers)
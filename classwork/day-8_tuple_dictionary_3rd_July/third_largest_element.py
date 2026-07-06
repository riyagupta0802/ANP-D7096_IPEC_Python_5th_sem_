'''---------- Third Largest Number in a List ------------------
Write a Python program to find the third largest
number from a list of 20 numbers entered by the user.'''

# create an empty list
lst = []
# input 20 numbers
for i in range(20):
    num = int(input("Enter Number : "))
    lst.append(num)
# sort the list in descending order
lst.sort(reverse=True)

# display third largest number
print("Third Largest Number :", lst[2])
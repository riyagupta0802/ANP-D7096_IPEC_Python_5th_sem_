'''Program to i/p any 10 numbers and display odd numbers among them'''

#'''Display Odd Numbers from 10 Numbers'''

# Creating a blank list
numbers = []

print("Enter any 10 numbers:")

for x in range(10):
    # Input of elements from the user
    num = int(input())
    # Inserting data in list at the end
    numbers.append(num)

#----------------------------------------
print("-------------------")
print("Numbers are :", numbers)

print("Odd numbers are :")
for i in numbers:
    if i % 2 != 0:
        print(i)

#---------------------------------------------

'''Output:-
Enter any 10 numbers:
1
2
3
4
5
6
7
8
9
10
-------------------
Numbers are : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Odd numbers are :
1
3
5
7
9
'''
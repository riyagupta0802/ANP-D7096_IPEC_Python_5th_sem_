'''Count Eligible Voters'''

# Creating a blank list
ages = []

print("Enter the age of 10 people:")

for x in range(10):
    # Input age from the user
    age = int(input())
    # Inserting data in list
    ages.append(age)

#----------------------------------------
print("-------------------")
print("Ages are :", ages)

# Counting eligible voters
count = 0
for i in ages:
    if i >= 18:
        count += 1

print("Total number of people eligible for voting are :", count)

#---------------------------------------------

'''Sample Output:-
Enter the age of 10 people:
15
18
20
17
25
30
16
19
18
14
-------------------
Ages are : [15, 18, 20, 17, 25, 30, 16, 19, 18, 14]
Total number of people eligible for voting are : 6
'''
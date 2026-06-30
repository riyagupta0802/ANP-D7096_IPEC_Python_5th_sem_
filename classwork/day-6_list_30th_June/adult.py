'''Count Adults from 15 People'''

# Creating a blank list
ages = []

print("Enter the age of 15 people:")

for x in range(15):
    # Input age from the user
    age = int(input())
    # Inserting data in list at the end
    ages.append(age)

#----------------------------------------
print("-------------------")
print("Ages are :", ages)

# Finding total adults
count = 0
for i in ages:
    if i > 18:
        count += 1

print("Total number of adults are :", count)

#---------------------------------------------

'''Output:-
Enter the age of 15 people:
15
20
18
25
30
17
19
22
16
40
18
21
14
50
13
-------------------
Ages are : [15, 20, 18, 25, 30, 17, 19, 22, 16, 40, 18, 21, 14, 50, 13]
Total number of adults are : 8
'''
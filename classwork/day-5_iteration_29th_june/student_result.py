'''---------- Student Result Analyzer -------------

Analyze marks of students.

Pass Marks = 40
Distinction Marks = 75

---------------------------------------------------'''

#--------------------------------------------------
#---------------- Coding --------------------------

n = int(input("Enter Number of Students : "))

total = 0
highest = -1
lowest = 101
passed = 0
distinction = 0

for i in range(n):

    marks = float(input("Enter Marks : "))

    total += marks

    if(marks > highest):
        highest = marks

    if(marks < lowest):
        lowest = marks

    if(marks >= 40):
        passed += 1

    if(marks >= 75):
        distinction += 1

average = total/n

print("Highest Marks :",highest)
print("Lowest Marks :",lowest)
print("Average Marks :",average)
print("Number of Students Passed :",passed)
print("Number of Students with Distinction :",distinction)

#--------------------------------------------------
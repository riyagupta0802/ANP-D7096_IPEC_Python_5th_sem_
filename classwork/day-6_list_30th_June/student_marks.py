'''Eligible Students for Admission (Age, Name & Marks)'''

# Creating blank lists
names = []
ages = []
marks = []

print("Enter details of 50 students:")

for x in range(50):
    # Input details
    name = input("Enter Name : ")
    age = int(input("Enter Age : "))
    mark = int(input("Enter Marks : "))

    # Storing data in lists
    names.append(name)
    ages.append(age)
    marks.append(mark)

#----------------------------------------
print("-------------------")
print("Students eligible for admission (Marks > 75):")

for i in range(50):
    if marks[i] > 75:
        print("Name :", names[i], "Age :", ages[i], "Marks :", marks[i])

#---------------------------------------------

'''Sample Output:-
Enter details of 50 students:

Enter Name : Riya
Enter Age : 19
Enter Marks : 85

Enter Name : Mans
Enter Age : 21
Enter Marks : 72

...

-------------------
Students eligible for admission (Marks > 75):

Name : Riya Age : 19 Marks : 85
...
'''
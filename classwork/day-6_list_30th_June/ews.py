'''EWS Category Eligibility'''

# Creating blank lists
names = []
salary = []

print("Enter details of 15 persons:")

for x in range(15):
    # Input details
    name = input("Enter Name : ")
    sal = float(input("Enter Salary (in LPA) : "))

    # Storing data in lists
    names.append(name)
    salary.append(sal)

#----------------------------------------
print("-------------------")
print("Persons eligible for EWS category (Salary > 5 LPA):")

for i in range(15):
    if salary[i] > 5:
        print("Name :", names[i], "Salary :", salary[i], "LPA")

#---------------------------------------------

'''Sample Output:-
Enter details of 15 persons:

Enter Name : Riya
Enter Salary (in LPA) : 6

Enter Name : Aman
Enter Salary (in LPA) : 4.5

Enter Name : Priya
Enter Salary (in LPA) : 8

-------------------
Persons eligible for EWS category (Salary > 5 LPA):

Name : Riya Salary : 6.0 LPA
Name : Priya Salary : 8.0 LPA
'''
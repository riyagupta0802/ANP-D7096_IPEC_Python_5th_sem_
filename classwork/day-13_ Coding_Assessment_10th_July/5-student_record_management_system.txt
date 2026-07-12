''' ---Student Record Management System---

Write a Python program to manage student records. 
Each student's data should contain: 
• Roll Number  
• Name  
• Marks  
Store all records using a dictionary where the roll number is the key. 
Display the following menu repeatedly: 
1. Add Student 
2. Search Student 
3. Display All Students 
4. Exit 
Requirements: 
• Use a while loop for the menu.  
• Use functions for each operation.  
• Display "Record Not Found" if the roll number does not exist.  
• Exit the program when the user selects option 4.  
-----------------------------------------------------------------------
Sample Output 
1. Add Student 
2. Search Student 
3. Display All Students 
4. Exit 
 
Enter Choice : 1 
 
Roll No : 101 
Name : Rahul 
Marks : 88 
 
Student Added Successfully 
 
Enter Choice : 2 
 
Enter Roll No : 101 
 
Roll No : 101 
Name : Rahul 
Marks : 88 
 
Enter Choice : 4 
 
Thank You
'''

# Student Record Management System

students = {}

# Function to add a student
def add_student():
    roll = input("Roll No: ")
    name = input("Name: ")
    marks = int(input("Marks: "))

    students[roll] = [name, marks]
    print("Student Added Successfully")


# Function to search a student
def search_student():
    roll = input("Enter Roll No: ")

    if roll in students:
        print("Roll No:", roll)
        print("Name:", students[roll][0])
        print("Marks:", students[roll][1])
    else:
        print("Record Not Found")


# Function to display all students
def display_students():
    if len(students) == 0:
        print("No Records Found")
    else:
        print("\nStudent Records")
        for roll in students:
            print("Roll No:", roll)
            print("Name:", students[roll][0])
            print("Marks:", students[roll][1])
            print()


# Main Program
while True:
    print("\n1. Add Student")
    print("2. Search Student")
    print("3. Display All Students")
    print("4. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        search_student()

    elif choice == 3:
        display_students()

    elif choice == 4:
        print("Thank You")
        break

    else:
        print("Invalid Choice")


'''Output:
1. Add Student 
2. Search Student 
3. Display All Students 
4. Exit 
 
Enter Choice : 1 
 
Roll No : 101 
Name : Rahul 
Marks : 88 
 
Student Added Successfully 
 
Enter Choice : 2 
 
Enter Roll No : 101 
 
Roll No : 101 
Name : Rahul 
Marks : 88 
 
Enter Choice : 4 
 
Thank You
'''

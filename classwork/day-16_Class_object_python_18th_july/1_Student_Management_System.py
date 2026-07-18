'''                                         -----------Student Management System-----------
Problem Statement:-
Create a class named Student to store and display a student's details.
#-------------------------------------------------------------------------
Requirements:-
1. Create a class Student.
2. Define the following instance variables:
    o student_id
    o name
    o course
    o marks
3. Create a method accept_data() to take input from the user.
4. Create a method display_data() to display all student details.
5. Create another method check_result() that:
    o Displays "Pass" if marks are 35 or above
    o Displays "Fail" otherwise.
6. Create an object of the class and call all the methods. 
#----------------------------------------------------------------
Sample Input
Enter Student ID : 101
Enter Name : Rahul
Enter Course : Python
Enter Marks : 78
Expected Output
------ Student Details ------
Student ID : 101
Name : Rahul
Course : Python
Marks : 78
Result : Pass

#---------------------------------------------------------------------------
'''

#Code---------------------------------------------------------------------------------

class Student:
    #define variables
    def __init__(student):
        student.student_id = 0
        student.name = ""
        student.course = ""
        student.marks = 0

    def accept_data(student):
        #taking input from the user
        student.student_id = int(input("Enter Student ID : "))
        student.name = input("Enter Name : ")
        student.course = input("Enter Course : ")
        student.marks = int(input("Enter Marks : "))

    def check_result(student):
        #check if student is pass or fail
        if student.marks >= 35:
            return "Pass"
        else:
            return "Fail"

    def display_data(student):
        #displaying the data of the students:-
        print("\n------ Student Details ------")
        print("Student ID :", student.student_id)
        print("Name       :", student.name)
        print("Course     :", student.course)
        print("Marks      :", student.marks)
        print("Result     :", student.check_result())

#object of the class
student1 = Student()
#calling all the methods
student1.accept_data()
student1.display_data()

'''Output

Enter Student ID : 101
Enter Name : Rahul
Enter Course : Python
Enter Marks : 78

------ Student Details ------
Student ID : 101
Name : Rahul
Course : Python
Marks : 78
Result : Pass

'''

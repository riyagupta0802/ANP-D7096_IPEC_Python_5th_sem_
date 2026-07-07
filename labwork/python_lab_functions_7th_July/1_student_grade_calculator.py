'''--------- Student Grade Calculator----------

Write a Python program that defines a function calculate_grade(marks). 
The function should: 
• Accept marks (0-100) as a parameter.  
• Return the grade according to the following criteria:  
o 90 and above → A+  
o 75-89 → A  
o 60-74 → B  
o 40-59 → C  
o Below 40 → Fail  
The main program should: 
• Accept marks of 5 students.  
• Call the function for each student.  
• Display the marks and corresponding grade.  '''


#function to calculate student grades
def calculate_grade(marks):
    if marks>=90:
        return "A+"
    elif marks>=75:
        return "A"
    elif marks>=60:
        return "B"
    elif marks>=40:
        return "C"  
    else:
        return "Fail"
#-----------------------------------------------
#Main Program
for i in range(1,6):
    marks=int(input("Enter marks of student " + str(i) + ": "))
    grade=calculate_grade(marks)
    print("Marks =", marks, "Grade =",grade)


'''
Output:
Enter marks of student 1: 98
Marks = 98 Grade = A+
Enter marks of student 2: 32
Marks = 32 Grade = Fail
Enter marks of student 3: 78
Marks = 78 Grade = A
Enter marks of student 4: 80
Marks = 80 Grade = A
Enter marks of student 5: 64
Marks = 64 Grade = B'''
'''---------Student Subject Report Card--------

Problem Statement: 
Create a nested dictionary to store marks of students in three subjects.

Example:
{ 
'Rahul': {'Math': 85, 'Science': 90, 'English': 88}, 
'Priya': {'Math': 78, 'Science': 95, 'English': 82}, 
'Ankit': {'Math': 91, 'Science': 89, 'English': 94} 
} 
Write a program to: 
• Calculate the total marks of each student.  
• Calculate the average marks of each student.  
• Display the topper based on total marks.  
• Display the subject-wise highest marks along with the student's name.  
• Display students whose average is greater than or equal to 85.'''


# initialize dictionary
students = {}

# input details of 3 students
for i in range(3):
    name = input("Enter Student Name: ")
    math = int(input("Enter Math Marks: "))
    science = int(input("Enter Science Marks: "))
    english = int(input("Enter English Marks: "))
    students[name] = {"Math": math, "Science": science, "English": english}
print("-------------------------------------------------")

# display student details
print("Student Report Card:")
for name in students:
    print(name, students[name])
print("-------------------------------------------------")

# calculate total and average
totalmarks = {}

print("Total and Average Marks:")
for name in students:
    total = students[name]["Math"] + students[name]["Science"] + students[name]["English"]
    average = total / 3
    totalmarks[name] = total
    print(name, "Total =", total, "Average =", average)
print("-------------------------------------------------")

# display topper
topper = max(totalmarks, key=totalmarks.get)
print("Topper:")
print(topper, totalmarks[topper])
print("-------------------------------------------------")

# subject-wise highest marks
subjects = ["Math", "Science", "English"]

print("Subject-wise Highest Marks:")
for subject in subjects:
    highest = 0
    student = ""
    for name in students:
        if students[name][subject] > highest:
            highest = students[name][subject]
            student = name
    print(subject, ":", student, highest)
print("-------------------------------------------------")

# display students with average >=85
print("Students with Average >= 85:")
for name in students:
    average = (students[name]["Math"] + students[name]["Science"] + students[name]["English"]) / 3
    if average >= 85:
        print(name, average)

'''Output:
Enter Student Name: Rahul
Enter Math Marks: 85
Enter Science Marks: 90
Enter English Marks: 88
Enter Student Name: Priya
Enter Math Marks: 78
Enter Science Marks: 95
Enter English Marks: 82
Enter Student Name: Ankit
Enter Math Marks: 91
Enter Science Marks: 89
Enter English Marks: 94
-------------------------------------------------
Student Report Card:
{
'Rahul': {'Math': 85, 'Science': 90, 'English': 88},
'Priya': {'Math': 78, 'Science': 95, 'English': 82},
'Ankit': {'Math': 91, 'Science': 89, 'English': 94}
}
-------------------------------------------------
Total and Average Marks:
Rahul Total = 263 Average = 87.66666666666667
Priya Total = 255 Average = 85.0
Ankit Total = 274 Average = 91.33333333333333
-------------------------------------------------
Topper:
Ankit 274
-------------------------------------------------
Subject-wise Highest Marks:
Math : Ankit 91
Science : Priya 95
English : Ankit 94
-------------------------------------------------
Students with Average >= 85:
Rahul 87.66666666666667
Priya 85.0
Ankit 91.33333333333333'''        
'''------------- Dictionary Search System--------------

Problem statement:
Write a Python program that defines a function search_student(student_dict, roll_no). 
The function should: 
• Accept a dictionary where:  
o Key = Roll Number  
o Value = Student Name  
• Search for the given roll number.  
• Return the student name if found; otherwise return "Student Not Found".  
The main program should: 
• Create a dictionary of at least 5 students.  
• Accept a roll number from the user.  
• Display the search result. 
'''

def search_student(student_dict, roll_no):
    if roll_no in student_dict:
        return student_dict[roll_no]
    else:
        return "Student Not Found"

# Main Program
student_dict = {}

for i in range(5):
    roll_no = int(input("Enter Roll Number: "))
    name = input("Enter Student Name: ")
    student_dict[roll_no] = name

search_roll = int(input("Enter Roll Number to Search: "))

print("Search Result:", search_student(student_dict, search_roll))


'''Output:
Enter Roll Number: 101
Enter Student Name: Rahul
Enter Roll Number: 102
Enter Student Name: Priya
Enter Roll Number: 103
Enter Student Name: Ankit
Enter Roll Number: 104
Enter Student Name: Neha
Enter Roll Number: 105
Enter Student Name: Riya
Enter Roll Number to Search: 101
Search Result: Rahul
'''
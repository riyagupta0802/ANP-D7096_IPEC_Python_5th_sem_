'''to calculate the number of complete rows that can be formed in a classroom'''

# input of total students from user
total_students = int(input("Enter the total number of students: "))

# input of students per row from user
students_per_row = int(input("Enter the number of students per row: "))

# calculation of complete rows
print("Number of Complete Rows is: ", total_students // students_per_row)
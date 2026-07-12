'''---Student Grade Analyzer---

Write a Python program that performs the following tasks: 
• Accept the student's name.  
• Accept marks of 5 subjects and store them in a list.  
• Calculate the total and percentage using a user-defined function.  
• Using selection statements, display the grade according to the following criteria: 
 
90 and above A+ 
75–89 A 
60–74 B 
40–59 C 
Below 40 Fail
------------------------------------------------------------------------------------------
Finally, display all entered marks along with total, percentage, and grade. 
-------------------------------------------------------------------------------------
Sample Input 
Enter Name: Rahul 
Enter Marks: 
80 
75 
90 
88 
70

'''

#Input Student's name
name = input("Enter Student's name: ")

#create a empty list
marks = []
print("Enter marks: ") 

for i in range(5):
    #input element from the user
    mark=int(input())
    #insert data in list at the end
    marks.append(mark)

# Calculate total and percentage
total = sum(marks)
percentage= total/5

#displaying data to the user
print("-------------------------------------")
print("Student name ",name)
print("Marks :", marks)
print("Total :",total)
print("Percentage:",percentage) 

# Determine grade
if(percentage>=90):
    print("Grade: A+")
elif(percentage>=75):
    print("Grade: A")
elif(percentage>=60):
    print("Grade: B")
elif(percentage>=40):
    print("Grade: C")
else:
    print("Grade: Fail")  
           


'''Output:-
Enter Student's name: Rahul 
Enter marks:
80
75
90
88
70
-------------------------------------
Student name  Rahul
Marks : [80, 75, 90, 88, 70]
Total : 403
Percentage: 80.6
Grade: A
'''
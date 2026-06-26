'''---------- Employee Performance Evaluation ------------------
An employee is evaluated using:

• Project Score
• Attendance Percentage
• Client Feedback Score

Rules:
• Excellent -> All scores above 90
• Good -> Scores above 75
• Average -> Scores above 60
• Poor -> Otherwise

Additional Rule:
• Attendance below 70% cannot receive more than
  Average rating.

---------------------------------------------------------------
Sample Input
Project Score : 95
Attendance : 65
Client Feedback : 92
---------------------------------------------------------------
Sample Output
Performance Rating : Average
Reason : Attendance below 70%
---------------------------------------------------------------'''
#--------------------------------------------------------------
#---------------- Coding --------------------------------------

project = int(input("Enter Project Score : "))
attendance = int(input("Enter Attendance Percentage : "))
feedback = int(input("Enter Client Feedback Score : "))

if(project < 0 or project > 100 or attendance < 0 or attendance > 100 or feedback < 0 or feedback > 100):
    exit("Invalid Input")

if(attendance < 70):
    print("Performance Rating : Average")
    print("Reason : Attendance below 70%")
else:
    if(project > 90 and attendance > 90 and feedback > 90):
        print("Performance Rating : Excellent")
    elif(project > 75 and attendance > 75 and feedback > 75):
        print("Performance Rating : Good")
    elif(project > 60 and attendance > 60 and feedback > 60):
        print("Performance Rating : Average")
    else:
        print("Performance Rating : Poor")

#--------------------------------------------------------------

''' Output :
Enter Project Score : 95
Enter Attendance Percentage : 65
Enter Client Feedback Score : 92

Performance Rating : Average
Reason : Attendance below 70%
'''
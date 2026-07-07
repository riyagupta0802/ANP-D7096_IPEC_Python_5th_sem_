'''----------- List Analysis using Functions----------------

Problem statement:
Write a Python program that defines the following functions: 
• find_max(numbers)  
• find_min(numbers)  
• find_average(numbers)  
The program should: 
• Accept a list of 10 integers from the user.  
• Call all three functions.  
• Display the maximum value, minimum value, and average of the list.  '''


def  find_max(numbers):
    return max(numbers)
def find_min(numbers):
    return min(numbers)
def find_average(numbers):
    return sum(numbers)/10
#--------------------------------
#main program
#create a blank list
numbers=[]
for i in range(10):
    #insert data in list
    num=int(input("Enter 10 number:"))
    #append data in list at the end
    numbers.append(num)  
#displaying find_max(numbers), find_min(numbers) ,  find_average(numbers)
print("Max value =" , find_max(numbers))
print("Min value=" , find_min(numbers))  
print("Avg =", find_average(numbers))  


'''
Output:

Enter 10 number:1
Enter 10 number:2
Enter 10 number:3
Enter 10 number:4
Enter 10 number:5
Enter 10 number:6
Enter 10 number:7
Enter 10 number:8
Enter 10 number:9
Enter 10 number:10
Max value = 10
Min value= 1
Avg = 5.5'''


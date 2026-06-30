'''Sum of 10 numbers'''
#Creating a blank list
numbers=[]
print("Enter any 10 numbers:")
for x in range(10):
    #Input of elements from the user
    num=int(input())
    #Inserting data in list at the end
    numbers.append(num)
    #----------------------------------------
    print("-------------------")
    print("Numbers are :"numbers)
    #Finding sum
    Sum=0
    for i in numbers:
        Sum+=i
        print("Sum of 10 numbers are :",Sum)

#---------------------------------------------

'''Output:-
Enter any 10 numbers:
1
2
3
4
5
6
7
8
9
10
#----------------------
Numbers are :[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Sum of 10 numbers are : 55'''        
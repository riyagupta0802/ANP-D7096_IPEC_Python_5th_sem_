'''Program to display elements of list in forward direction using backward direction'''

#Creating a blank list
numbers=[]
print("Enter any 10 numbers:")
for i in range(10):
    #Input of elements from the user
    num=int(input())
    #Inserting data in list at the end
    numbers.append(num)
#------------------------------------------
print("--------------------")
print("Numbers are :", numbers)
for i in range(-len(numbers), 0):
    print("Numbers in forward direction are :", numbers[i])


'''
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
-----------------------
Numbers are : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Numbers in forward direction are : 1
Numbers in forward direction are : 2
Numbers in forward direction are : 3
Numbers in forward direction are : 4
Numbers in forward direction are : 5
Numbers in forward direction are : 6
Numbers in forward direction are : 7
Numbers in forward direction are : 8
Numbers in forward direction are : 9
Numbers in forward direction are : 10'''        
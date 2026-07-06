'''Create a tuple of 15 numbers given by use and display the odd numbers present in the tuple'''

#Creating a blank list
numbers_lst=[]
print("Enter any 15 numbers:")
for i in range(15):
    #input of elements from rhe user
    num=int(input())
    #inserting the elements in the list
    numbers_lst.append(num)
#---------------------------------------------------------    
    #converting the list into tuple
    numbers=tuple(numbers_lst)
    #displaying the tuple
    print("-----------------------")
    print("Tuple of 15 numbers:")
    print(numbers)
    #displaying the odd numbers
    print("-----------------------")
    print("Odd numbers in the tuple:")
    for element in numbers:
        if(element%2!=0):
            print(element, end=',')
            


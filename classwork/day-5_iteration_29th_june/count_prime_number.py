'''---------- Count Prime Numbers -----------------

Display all prime numbers within a range and
count total prime numbers.

---------------------------------------------------'''

#--------------------------------------------------
#---------------- Coding --------------------------

start = int(input("Enter Starting Number : "))
end = int(input("Enter Ending Number : "))

count = 0

print("Prime Numbers : ")

for num in range(start,end+1):

    if(num > 1):

        for i in range(2,num):
            if(num % i == 0):
                break
        else:
            print(num,end=" ")
            count += 1

print("\nTotal Prime Numbers :",count)

#--------------------------------------------------
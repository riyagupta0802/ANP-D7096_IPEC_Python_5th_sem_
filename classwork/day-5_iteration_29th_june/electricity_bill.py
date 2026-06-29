'''---------- Electricity Bill Analysis -----------

Analyze electricity consumption of N houses.

---------------------------------------------------'''

#--------------------------------------------------
#---------------- Coding --------------------------

n = int(input("Enter Number of Houses : "))

total = 0
highest = -1
lowest = 999999

for i in range(n):

    units = int(input("Enter Units Consumed : "))

    total += units

    if(units > highest):
        highest = units

    if(units < lowest):
        lowest = units

average = total/n

print("Total Units Consumed :",total)
print("Average Units Consumed :",average)
print("Highest Consumption :",highest)
print("Lowest Consumption :",lowest)

#--------------------------------------------------
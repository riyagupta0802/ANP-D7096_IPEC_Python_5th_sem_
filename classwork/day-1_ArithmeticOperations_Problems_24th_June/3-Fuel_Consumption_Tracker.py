'''to calculate the average fuel consumption (mileage) of a car'''

# input of total distance traveled from user
total_distance = float(input("Enter the total distance traveled (in km): "))

# input of fuel consumed from user
fuel_consumed = float(input("Enter the fuel consumed (in liters): "))

# calculation of average mileage
print("Average mileage of the car is: ", total_distance / fuel_consumed, "km/l")
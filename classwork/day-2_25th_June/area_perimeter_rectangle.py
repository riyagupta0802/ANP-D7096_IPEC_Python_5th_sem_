'''To calculate area and perimeter of a rectangle'''
#input of length from the user
length = float(input("Enter the length of the rectangle (in units): "))
#validating the length
if length < 0:
    exit("Length cannot be negative.")
#input of width from the user
width = float(input("Enter the width of the rectangle (in units): "))
#validating the width
if width < 0:
    exit("Width cannot be negative.")
#-----------------------------------------------------
#Displaying data to the user
print("Length of the rectangle: ", length, "units")
print("Width of the rectangle: ", width, "units")
#-----------------------------------------------------
#displaying area and perimeter of the rectangle
print("Area of the rectangle: ", length * width, "square units")
print("Perimeter of the rectangle: ", 2 * (length + width), "units")
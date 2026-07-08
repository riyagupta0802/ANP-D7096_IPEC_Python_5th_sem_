# operations.py

# Import module
import twodfigures

# Repeat until exit
while True:

    # Display menu
    print("------ Geometry Calculator ------")
    print("1. Square")
    print("2. Circle")
    print("3. Triangle")
    print("4. Rectangle")
    print("5. Exit")

    # Enter figure choice
    choice = int(input("Enter your choice: "))

    # Exit the program
    if choice == 5:
        print("Thank You!")
        break

    # Display operation menu
    print("1. Area")
    print("2. Perimeter")

    # Enter operation choice
    op = int(input("Enter your choice: "))

    # Square
    if choice == 1:
        side = float(input("Enter side: "))

        if op == 1:
            print("Area =", twodfigures.square_area(side))
        elif op == 2:
            print("Perimeter =", twodfigures.square_perimeter(side))
        else:
            print("Invalid Choice")

    # Circle
    elif choice == 2:
        radius = float(input("Enter radius: "))

        if op == 1:
            print("Area =", twodfigures.circle_area(radius))
        elif op == 2:
            print("Circumference =", twodfigures.circle_perimeter(radius))
        else:
            print("Invalid Choice")

    # Triangle
    elif choice == 3:

        # Area
        if op == 1:
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            print("Area =", twodfigures.triangle_area(base, height))

        # Perimeter
        elif op == 2:
            side1 = float(input("Enter side 1: "))
            side2 = float(input("Enter side 2: "))
            side3 = float(input("Enter side 3: "))
            print("Perimeter =", twodfigures.triangle_perimeter(side1, side2, side3))

        else:
            print("Invalid Choice")

    # Rectangle
    elif choice == 4:
        length = float(input("Enter length: "))
        breadth = float(input("Enter breadth: "))

        if op == 1:
            print("Area =", twodfigures.rectangle_area(length, breadth))
        elif op == 2:
            print("Perimeter =", twodfigures.rectangle_perimeter(length, breadth))
        else:
            print("Invalid Choice")

    # Wrong choice
    else:
        print("Invalid Choice")

    # Blank line
    print()


'''Output:
------ Geometry Calculator ------
1. Square
2. Circle
3. Triangle
4. Rectangle
5. Exit
Enter your choice: 4
1. Area
2. Perimeter
Enter your choice: 2
Enter length: 12
Enter breadth: 10
Perimeter = 44.0

------ Geometry Calculator ------
1. Square
2. Circle
3. Triangle
4. Rectangle
5. Exit
Enter your choice: 2
1. Area
2. Perimeter
Enter your choice: 1
Enter radius: 12.4
Area = 483.0512864159666

------ Geometry Calculator ------
1. Square
2. Circle
3. Triangle
4. Rectangle
5. Exit
Enter your choice: 5
Thank You!
'''    
#Accept input from a user asking the number of sides of a shape (up to hexagon), then ask for the length of the side, and then print out the area of the shape.
import math

shapeSides = 0
sideLength = 0
counter = 1

while counter != 0:
    try:
        shapeSides = input("Enter the number of sides of the shape: ")
        shapeSides = int(shapeSides)
        if (shapeSides <= 2):
            print("Please enter a number of sides greater than 2 and less than 7")
        elif (shapeSides > 6):
            print("Please enter a number of sides greater than 2 and less than 7")
        else:
            counter == 0
            try:
                sideLength = input("Please enter the length of one side: ")
                sideLength = float(sideLength)
                if shapeSides == 3:
                    print('This shape is a triangle, and this is the area: ', "{:.2f}".format((math.sqrt(3) / 4) * (sideLength * sideLength)))
                elif shapeSides == 4:
                    print('This shape is a square, and this is the area: ', "{:.2f}".format((sideLength * sideLength)))
                elif shapeSides == 5:
                    print('This shape is a pentagon, and this is the area: ', "{:.2f}".format(((1 / 4)) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * (sideLength * sideLength)))
                elif shapeSides == 6:
                    print('This shape is a hexagon, and this is the area: ', "{:.2f}".format(((3 * math.sqrt(3)) / 2) * (sideLength * sideLength)))
            except ValueError:
                print("Please enter a number")
    except ValueError:
        print("Please enter a number")

programPause = input("Press the <ENTER> key to continue...")

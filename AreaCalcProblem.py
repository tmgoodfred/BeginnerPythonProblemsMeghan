#Accept input from a user asking the number of sides of a shape (up to hexagon), then ask for the length of the side, and then print out the area of the shape.
import math

checker = 1
while checker != 0:
    shapeSides = input("Enter the number of sides of the shape: ")
    try:
        val2 = int(shapeSides)
        if (val2 <= 2 and val2 > 6):
            print("Please enter a number of sides greater than 2 and less than 7")
        else:
            checker = 0
    except ValueError:
        print("Please enter a number")

checker2 = 1
sideLength = input("Please enter the length of one side: ")
try:
    val = float(sideLength)
    if val2 == 3:
        print('This shape is a triangle, and this is the area: ', "{:.2f}".format((math.sqrt(3) / 4) * (val * val)))
    elif val2 == 4:
        print('This shape is a square, and this is the area: ', "{:.2f}".format((val * val)))
    elif val2 == 5:
        print('This shape is a pentagon, and this is the area: ', "{:.2f}".format(((1 / 4)) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * (val * val)))
    elif val2 == 6:
        print('This shape is a hexagon, and this is the area: ', "{:.2f}".format(((3 * math.sqrt(3)) / 2) * (val * val)))
except ValueError:
    print("Please enter a number")

programPause = input("Press the <ENTER> key to continue...")
#Ask the user to input a number, return if the number given is odd or even, and if the number is 69 or 420 output "ayyy lmao"

numCheck = input("Please enter a number: ")
try:
    val = int(numCheck)
    if(val % 2 == 0):
        print("You entered: ",val, " which is even")
    else:
        print("You entered: ",val, " which is odd")
    if (val == 69):
        print("ayyy lmao")
    elif (val == 420):
        print("ayyy lmao")
except ValueError:
    print("Please enter a valid single digit number")

programPause = input("Press the <ENTER> key to continue...")
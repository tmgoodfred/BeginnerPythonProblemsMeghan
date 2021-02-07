#Ask the user to enter 5 names of animals, sort the list of names alphabetically in reverse order, and output them to the user.

animalArray = []
for x in range(5):
    animalArray.append(input("Enter an animal name: "))

animalArray.sort()
animalArray.reverse()
print(animalArray)

programPause = input("Press the <ENTER> key to continue...")
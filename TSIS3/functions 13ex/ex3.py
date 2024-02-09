numberOfHeads = int(input('Enter the total number of heads: '))
numberOfLegs = int(input('Enter the total number of legs: '))
def solve(headsNumber, legsNumber):
    if headsNumber == 0 or legsNumber % 2 !=0 or headsNumber > legsNumber:
        print("Impossible")
    else:  
        howManyRabbits = int((legsNumber + (-2 * headsNumber))/2)
        howManyChickens = int(headsNumber - howManyRabbits)
        print('We have {} chickens & {} rabbits.'.format(howManyChickens, howManyRabbits))
solve(numberOfHeads, numberOfLegs)
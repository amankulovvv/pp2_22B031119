import random
guessNumber = random.randint(1,20)
myName = input("Hello! What's your name?\n")
print("Well, {}, I am thinking of a number between 1 and 20.".format(myName))
myGuess = 0
count = 1
while myGuess != guessNumber:
    myGuess = int(input("Take a guess.\n"))
    if myGuess > guessNumber:
        print("Your guess is too high.")
        count += 1
    elif myGuess < guessNumber:
        print("Your guess is too low.")
        count += 1
    else:
        print("Good job, {}! You guessed my number in {} guesses!".format(myName,count))


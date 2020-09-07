
#This is a 'guess the number' game.

import random

print("Hello there. What is your name?")
name = input()

print("Well, " + name + ", I am thinking of a number between 1 and 20")
#Now generate a random number between 1 and 20 inclusive.

secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7): #starting at 1 but not including 7, so 6 guesses
	print("Take a guess.")
	guess = int(input()) #must turn it to an integer

	if guess < secretNumber:
		print("Your guess is  too low, try again. You have " + str(6 - guessesTaken) + " tries left.")
	elif guess > secretNumber:
		print("Your guess is too high, try again. You have " + str(6 - guessesTaken) + " tries left.")
	else: #if they guess the correct number
		break #break statement caused the execution to break out of the loop prematurely

if guess == secretNumber:
	print("Good job, " + name + "! You guessed my number in " + str(guessesTaken) + " tries.")
else:
	print("Sorry, the number I was thinking of was "  + str(secretNumber) + ".")

	

#####----- High/Low start -----#####
def highLow():
	import random

	maximum = False

	while maximum == False:
		print("\n\n\nWhat would you like the maximum number to be?")
		try:
			maximum = int(input("\n> "))
			if maximum == 1:
				raise NameError
			print("\n\nStarting High/Low with a maximum of " + str(maximum) + "\n.\n.\n.\n")
		except (NameError):
			print("\"1\" cannot be used as the maximum number!")
			maximum = False
		except:
			print("Invalid input!")

	number = random.randrange(0, maximum)
	guessCount = 0
	guessCheck = 0
	prevError = False
	guess = ""

	# Starts out with empty guess variable. Breaks loop once a valid guess is inputted. This is so the error handling works as intended
	while guess == "":
		try:
			guess = int(input("Please enter your guess: "))
			if guess < 0 or guess > maximum:
				print("Error: Guess outside of range!\n\n")
				guess = ""
		except:
			print("\nError: Invalid input!\n\n")

	while guess != number:
		try:
			if guess < 0 or guess > maximum:
				print("Error: Guess outside of range!\n\n")
				prevError = True
				guess = guessCheck
				if guessCount >= 0:
					guessCount -= 1
			if guess < number:
				if prevError == True:
					print("Your previous valid guess, " + str(guess) + ", was too low")
					prevError = False
				else:
					print("Your guess is too low, try again")
			else:
				if prevError == True:
					print("Your previous valid guess, " + str(guess) + ", was too high")
					prevError = False
				else:
					print("Your guess is too high, try again")
			guessCount += 1
			guessCheck = guess
			print("Number of guesses: " + str(guessCount) + "\n")
			guess = int(input("Please enter your guess: "))
			if guess == number:
				print("Hit!")
				print("It took you " + str(guessCount) + " guesses")
				break
		except:
			print("Error: Invalid input!\n\n")
			prevError = True
			if guessCount >= 0:
				guessCount -= 1
			if guess == number:
				print("Hit!")
				print("It took you " + str(guessCount) + " guesses")
				break
#####----- High/Low end -----#####
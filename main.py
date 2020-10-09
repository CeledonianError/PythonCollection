# Import all the programs
import highLow
import madLib
import simpleCalc
import pythonWho
import massCalc

#####-----~@~-----#####
def start():
	print("Welcome to Error's Python Collection. \nPlease select a mini program. \n\n[1] High/Low Guessing Game \n[2] Mad Lib  \n[3] Simple Calculator \n[4] Python Who: Choose Your Own Adventure\n[5] Unknown Mass Calculator\n\nTo quit, type \"quit\"")

	selOptions = ["quit", "1", "2", "3", "4", "5"]
	sel = [input("\n> ")]
	selQuit = False

	while True:
		if sel[0] not in selOptions:
			print("\nThat is not a valid option! Try again")
			sel = [input("\n> ")]

		if sel[0] in selOptions:
			if sel[0] == selOptions[1]:
				print("\nYou have selected High/Low Guessing Game \n\nWhat would you like the maximum number to be?")
				try:
					maxHigh = input("\n> ")
					print("\n\nStarting High/Low with a maximum of " + maxHigh + "\n.\n.\n.\n")
					highLow.highLow(maxHigh)
					print("\n\n\n.\n.\n.\n")
					start()
				except:
					print("Invalid input!")

			elif sel[0] == selOptions[2]:
				print("\nYou have selected Mad Lib \n.\n.\n.\n")
				madLib.madLib()
				print("\n\n\n.\n.\n.\n")
				start()

			elif sel[0] == selOptions[3]:
				print("\nYou have selected Simple Calculator\n.\n.\n.\n")
				simpleCalc.simpleCalc()
				print("\n\n\n.\n.\n.\n")
				start()
			elif sel[0] == selOptions[4]:
				print("\nYou have selected Python Who: Choose Your Own Adventure\n.\n.\n.\n")
				pythonWho.pythonWho()
				print("\n\n\n.\n.\n.\n")
				start()

			elif sel[0] == selOptions[5]:
				print("\nYou have selected Unknown Mass Calculator\n.\n.\n.\n")
				massCalc.massCalc()
				print("\n\n\n.\n.\n.\n")
				start()
				
			else:
				print("Are you sure you want to quit? Y/N")
				selQuit = input("\n> ")
				if selQuit == "Y" or selQuit == "y":
					quit()
				else:
					print("\n\n\n")
					start()
#####-----~@~-----#####

start()

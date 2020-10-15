# Import all the programs
import highLow
import madLib
import simpleCalc
import pythonWho
import massCalc
import ticTacToe

#####-----~@~-----#####
def start():
	print("Welcome to Error's Python Collection. \nPlease select a mini program. \n\n[1] High/Low Guessing Game \n[2] Mad Lib  \n[3] Simple Calculator \n[4] Python Who: Choose Your Own Adventure\n[5] Unknown Mass Calculator\n[6] Tic Tac Toe\n\nTo quit, type \"quit\"")

	selOptions = ["quit", "1", "2", "3", "4", "5", "6"]
	sel = input("\n> ")
	selQuit = False
	selOptionsNames = ["", "High Low Guessing Game", "Mad Lib", "Simple Calculator", "Python Who: Choose Your Own Adventure", "Unknown Mass Calculator", "Tic Tac Toe"]
	selFunctions = ["", highLow.highLow, madLib.madLib, simpleCalc.simpleCalc, pythonWho.pythonWho, massCalc.massCalc, ticTacToe.ticTacToe]
	selNames = selOptionsNames[int(sel)]

	while True:
		if sel not in selOptions:
			print("\nThat is not a valid option! Try again")
			sel = input("\n> ")

		print("\n.\n.\n.")
		print("You have selected " + selNames)
		print("\n-----~~~~~=~~~~~-----")
		selFunctions[int(sel)]()
		print("\n-----~~~~~=~~~~~-----\n")
		start()

		if sel == "quit":
			print("Are you sure you want to quit? Y/N")
			selQuit = input("\n> ")
			if selQuit == "Y" or selQuit == "y":
				quit()
			else:
				print("\n\n\n")
				start()
#####-----~@~-----#####

start()
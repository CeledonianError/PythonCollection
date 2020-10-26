# Import all the programs
import highLow
import madLib
import simpleCalc
import pythonWho
import massCalc
import ticTacToe
import ultimateTicTacToe
import regenAdventure
import decayBoard

#####-----~@~-----#####
def start():
	print("Welcome to Error's Python Collection. \nPlease select a mini program. \n")
	print("[1] High/Low Guessing Game")
	print("[2] Mad Lib") 
	print("[3] Simple Calculator")
	print("[4] Python Who: Choose Your Own Adventure")
	print("[5] Unknown Mass Calculator")
	print("[6] Tic Tac Toe")
	print("[7] Ultimate Tic Tac Toe")
	print("[8] Regeneration: A Text-Based RPG")
	print("[9] Five \'Till Decay: A Random Chance Board Game")
	print("\nTo quit, type \"quit\"")

	selOptions = ["quit", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
	sel = input("\n> ")
	selQuit = False
	selOptionsNames = ["", "High Low Guessing Game", "Mad Lib", "Simple Calculator", "Python Who: Choose Your Own Adventure", "Unknown Mass Calculator", "Tic Tac Toe", "Ultimate Tic Tac Toe", "Regeneration: A Text-Based RPG", "Five \'Till Decay: A Random Chance Board Game"]
	selFunctions = ["", highLow.highLow, madLib.madLib, simpleCalc.simpleCalc, pythonWho.pythonWho, massCalc.massCalc, ticTacToe.ticTacToe, ultimateTicTacToe.ultimateTicTacToe, regenAdventure.regenAdventure, decayBoard.decayBoard]

	while True:
		if sel not in selOptions:
			print("\nThat is not a valid option! Try again")
			sel = input("\n> ")

		if sel == "quit":
			print("Are you sure you want to quit? Y/N")
			selQuit = input("\n> ")
			if selQuit == "Y" or selQuit == "y":
				quit()
			else:
				print("\n\n\n")
				start()

		selName = selOptionsNames[int(sel)]
		print("\n.\n.\n.")
		print("You have selected " + selName)
		print("\n-----~~~~~=~~~~~-----")
		selFunctions[int(sel)]()
		print("\n-----~~~~~=~~~~~-----\n")
		start()
#####-----~@~-----#####

start()
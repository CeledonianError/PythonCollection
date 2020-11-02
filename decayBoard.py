board = [
	["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
	["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
	["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
	["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
	["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
	["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
	["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
	["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
	["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
	["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"]
	]

def decayBoard():
	import random
	class gameOver(Exception): pass

	# Player: Ⓧ
	# Select: ▽
	print("")
	print("      -~--~=={([ Five \'Till Decay ])}==~-~-~--")
	print("A random chance board game about getting five in a row")
	print("- - - - - - - ~ ~ ~ = = □ = = ~ ~ ~ - - - - - - -")
	print("\nHow to play:")
	print("▅  Each round, the board will decay\n")
	print("Ⓧ  Your goal? Make a row or column of 5 before it\'s too late.\n")
	print("▽  Select tiles by column (top) and row (right).\n")
	print("☠  Warning: If you select a tile that\'s already taken, your turn will be skipped.\n")
	print("- - - - - - - ~ ~ ~ = = □ = = ~ ~ ~ - - - - - - -")
	print("Now that you\'re familiar with the rules, please choose a difficulty. \n\nThe scale is as follows:\n")
	print("-~={ 3 ---~--- 5 ---~--- 10 }=~-")
	print("[3] Easy | [5] Normal | [10] Hard")

	# 3 - Easy, 5 - Normal, 10 - Hard, anything more = impossible?
	while True:
		try:
			decayRate = int(input("\n> "))
			break
		except:
			print("Invalid input! Try again!")


	# Random blocks
	def decayBoard():
		for i in range(decayRate):
			randX = random.randint(0, 9)
			randY = random.randint(0, 9)
			if board[randY][randX] == "□":
				board[randY][randX] = "▅"

	# Board print
	def printBoard():
		yPos = -1
		print("  [0]  [1]  [2]  [3]  [4]  [5]  [6]  [7]  [8]  [9]")
		print("   v    v    v    v    v    v    v    v    v    v")
		for i in board:
			for j in i:
				print("   " + str(j), end = " ")
			yPos += 1
			print("< [" + str(yPos) + "]\n")
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

	# Find winning rows
	def findFiveRow(row):
		success = 0
		for i in range(10):
			# Ignore out of range errors
			try:
				board[row][i + 1]
			except:
				continue
			# Check for lines of 5
			if board[row][i] == "Ⓧ" and board[row][i + 1] == "Ⓧ":
				success += 1
			if success >= 4:
				return True

	# Find winning columns 
	def findFiveCol(col):
		success = 0
		for i in range(10):
			# Ignore out of range errors
			try:
				board[i + 1][col]
			except:
				continue
			# Check for lines of 5
			if board[i][col] == "Ⓧ" and board[i + 1][col] == "Ⓧ":
				success += 1
			if success >= 4:
				return True

	# Input
	def playerInput():
		global board
		printBoard()
		print("")

		try:
			inputY = int(input("Column: "))
			inputX = int(input("Row: "))
			if board[inputX][inputY] == "□":
				board[inputX][inputY] = "▽"
				printBoard()
				# Confirm that the player wants to set tile
				confirm = input("\n▽ Are you happy with this choice? Y/N\n> ").lower()
				print("")
				if confirm == "y":
					board[inputX][inputY] = "Ⓧ"
				else:
					board[inputX][inputY] = "□"
					playerInput()
			else:
				print("\nThat tile has been taken.\n")
		except:
			print("\nInvalid input! Try again!\n")
			playerInput()

	# Print win
	def checkWin():
		for i in range(10):
			if findFiveRow(i):
				print("Row win")
				raise gameOver

			if findFiveCol(i):
				print("Column win")
				raise gameOver

	tilesDecayed = 0

	while True:
		for i in board:
			for j in i:
				if j == "□":
					tilesDecayed += 0
				else:
					tilesDecayed += 1

		if tilesDecayed >= 100:
			print("\nThe board cumbles away. You did not get 5 in a row. You loose.")
			print("\nGood bye.")
			break
		else:
			tilesDecayed = 0

		decayBoard()
		playerInput()
		try:
			checkWin()
		except gameOver:
			print("\nThe board cumbles away...")
			break
board = [
	["[01]", "[02]", "[03]", "[04]", "[05]"],
	["[06]", "[07]", "[08]", "[09]", "[10]"],
	["[11]", "[12]", "[13]", "[14]", "[15]"],
	["[16]", "[17]", "[18]", "[19]", "[20]"],
	["[21]", "[22]", "[23]", "[24]", "[25]"]
	]
turnCount = 0

def ultimateTicTacToe():
	print("")
	
	namePlayerX = input("Player X! What is your name?\n\n> ")
	namePlayerO = input("\nPlayer O! What is your name? \n\n> ")

	print("\nAlright " + namePlayerX + " and " + namePlayerO + ", let's play some Ultimate Tic Tac Toe!\n")

	### Player X start ###
	def xSelect():
		# Player X's turn
		global select
		global turnCount
		try:
			select = int(input("\n" + namePlayerX + " x~> ")) - 1
		# Check if space is already taken:
			if board[select // 5][select % 5] == "{xx}" or board[select // 5][select % 5] == "{oo}":
				print("That space is already taken!")
				xSelectError()
		# If empty, replace with current player's letter
			else:
				board[select // 5][select % 5] = "{xx}"
				turnCount += 1

		except IndexError:
			print(str(select + 1) + " isn't an option!\n")
			xSelectError()
		except ValueError:
			print("Invalid input!\n")
			xSelectError()
		print("")
	### Player X end ###

	### Player O start ###
	def oSelect():
		# Player O's turn
		global select
		global turnCount
		try:
			select = int(input("\n" + namePlayerO +" o~> ")) - 1
		# Check if space is already taken:
			if board[select // 5][select % 5] == "{xx}" or board[select // 5][select % 5] == "{oo}":
				print("That space is already taken!")
				oSelectError()
		# If empty, replace with current player's letter
			else:
				board[select // 5][select % 5] = "{oo}"
				turnCount += 1

		except IndexError:
			print(str(select + 1) + " isn't an option!\n")
			oSelectError()
		except ValueError:
			print("Invalid input!\n")
			oSelectError()
		print("")
	### Player O end ###

		

	### Win check start ###
	def checkRows(row, player):
		if all(i == player for i in board[row]):
			return True

	def checkDiagonals(player):
		if board[2][2] == player:
			if board[0][0] == player and board[1][1] == player and board[3][3] == player and board[4][4] == player:
				return True
		
			if board[0][4] == player and board[1][3] == player and board[3][1] == player and board[4][0] == player:
				return True

	def checkColumns(column, player):
		if board[0][column] == player:
			if board[1][column] == player:
				if board[2][column] == player:
					if board[3][column] == player:
						if board[4][column] == player:
							return True

	def sayXWins():
		displayBoard()
		print(namePlayerX + " wins!")
		print("----------")

	def sayOWins():
		displayBoard()
		print(namePlayerO + " wins!")
		print("----------")

	def winCheck():
	## Check X:
		# Check rows:
		if checkRows(0, "{xx}") or checkRows(1, "{xx}") or checkRows(2, "{xx}"):
			sayXWins()
			return True

		# Check diagonals:
		if checkDiagonals("{xx}"):
			sayXWins()
			return True

		# Check columns:
		if checkColumns(0, "{xx}") or checkColumns(1, "{xx}") or checkColumns(2, "{xx}"):
			print(namePlayerX + " wins!")
			sayXWins()
			return True

	## Check O:
		# Check rows:
		if checkRows(0, "{oo}") or checkRows(1, "{oo}") or checkRows(2, "{oo}"):
			sayOWins()
			return True

		# Check diagonals:
		if checkDiagonals("{xx}"):
			sayOWins()
			return True

		# Check columns:
		if checkColumns(0, "{oo}") or checkColumns(1, "{oo}") or checkColumns(2, "{oo}"):
			sayOWins()
			return True
	### Win check end ###

	def displayBoard():
		# Displays the game board
		print("----------")
		print(board[0][0], board[0][1], board[0][2], board[0][3], board[0][4])
		print(board[1][0], board[1][1], board[1][2], board[1][3], board[1][4])
		print(board[2][0], board[2][1], board[2][2], board[2][3], board[2][4])
		print(board[3][0], board[3][1], board[3][2], board[3][3], board[3][4])
		print(board[4][0], board[4][1], board[4][2], board[4][3], board[4][4])
		print("----------")

	def oSelectError():
		# Called if an error occurs while it's player O's turn
		displayBoard()
		oSelect()

	def xSelectError():
		# Called if an error occurs while it's player X's turn
		displayBoard()
		xSelect()


	while True:
		# Loops until someone wins or board gets filled
		displayBoard()
		xSelect()
		if turnCount == 25:
			print("----------")
			print("Cat's game!")
			print("----------")
			break
		if winCheck():
			break
		displayBoard()
		oSelect()
		if turnCount == 25:
			print("----------")
			print("Cat's game!")
			print("----------")
			break
		if winCheck():
			break
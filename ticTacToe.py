board = [
	["[1]", "[2]", "[3]"],
	["[4]", "[5]", "[6]"],
	["[7]", "[8]", "[9]"]
]
turnCount = 0

def ticTacToe():
	print("")
	
	namePlayerX = input("Player X! What is your name?\n\n> ")
	namePlayerO = input("\nPlayer O! What is your name? \n\n> ")

	print("\nAlright " + namePlayerX + " and " + namePlayerO + ", let's play some Tic Tac Toe!\n")

	board = [
		["[1]", "[2]", "[3]"],
		["[4]", "[5]", "[6]"],
		["[7]", "[8]", "[9]"]
	]

	### Player X start ###
	def xSelect():
		# Player X's turn
		global select
		global turnCount
		try:
			select = int(input("\n" + namePlayerX + " x~> ")) - 1
		# Check if space is already taken:
			if board[select // 3][select % 3] == "{x}" or board[select // 3][select % 3] == "{o}":
				print("That space is already taken!")
				xSelectError()
		# If empty, replace with current player's letter
			else:
				board[select // 3][select % 3] = "{x}"
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
			if board[select // 3][select % 3] == "{x}" or board[select // 3][select % 3] == "{o}":
				print("That space is already taken!")
				oSelectError()
		# If empty, replace with current player's letter
			else:
				board[select // 3][select % 3] = "{o}"
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

	def checkDiagonal(corner1, corner2, player):
		if board[0][corner1] == player and board[2][corner2] == player and board[1][1] == player:
			return True

	def checkColumns(column, player):
		if board[0][column] == player:
			if board[1][column] == player:
				if board[2][column] == player:
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
		if checkRows(0, "{x}") or checkRows(1, "{x}") or checkRows(2, "{x}"):
			sayXWins()
			return True

		# Check diagonals:
		if checkDiagonal(0, 2, "{x}") or checkDiagonal(2, 0, "{x}"):
			sayXWins()
			return True

		# Check columns:
		if checkColumns(0, "{x}") or checkColumns(1, "{x}") or checkColumns(2, "{x}"):
			print(namePlayerX + " wins!")
			sayXWins()
			return True

	## Check O:
		# Check rows:
		if checkRows(0, "{o}") or checkRows(1, "{o}") or checkRows(2, "{o}"):
			sayOWins()
			return True

		# Check diagonals:
		if checkDiagonal(0, 2, "{o}") or checkDiagonal(2, 0, "{o}"):
			sayOWins()
			return True

		# Check columns:
		if checkColumns(0, "{o}") or checkColumns(1, "{o}") or checkColumns(2, "{o}"):
			print(namePlayerX + " wins!")
			sayOWins()
			return True

		# Check columns:
		if checkColumns(0, "{o}") or checkColumns(1, "{o}") or checkColumns(2, "{o}"):
			sayOWins()
			return True
	### Win check end ###

	def displayBoard():
		# Displays the game board
		print("----------")
		print(board[0][0], board[0][1], board[0][2])
		print(board[1][0], board[1][1], board[1][2])
		print(board[2][0], board[2][1], board[2][2])
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
		if turnCount == 9:
			print("----------")
			print("Cat's game!")
			print("----------")
			break
		if winCheck():
			break
		displayBoard()
		oSelect()
		if turnCount == 9:
			print("----------")
			print("Cat's game!")
			print("----------")
			break
		if winCheck():
			break
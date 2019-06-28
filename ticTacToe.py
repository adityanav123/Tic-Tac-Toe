board = [' ' for x in range(10)] # Tic tac toe board

def insertLetter(letter, position):
	board[position] = letter 
def spaceIsFree(position):
	return board[position] == ' ' 
def printBoard(board):
	print('   |  | ')
	print(' ' + board[1] + ' |' + board[2] + ' | ' + board[3])
	print('-----------')
	print('   |  | ')
	print(' ' + board[4] + ' |' + board[5] + ' | ' + board[6])
	print('-----------')
	print(' ' + board[7] + ' |' + board[8] + ' | ' + board[9])
	print('   |  | ')

def isWinner(bo, le): # bo - board , # le - letter
	return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)
def playerMove():
	run = True
	while run:
		move = input('Select A position > (1 to 9)')
		try:
			move = int(move) # valid move check
			if move > 0 and move < 10:
				if spaceIsFree(move):
					run = False
					insertLetter('X', move)
				else: print('Space Occupied!.')
			else: print('No. not in the range 1 - 9 !., Try Again.')
		except: print('Type an integer!.')
def compMove(): # AI 
	possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0] # list of all possible moves at that point of time
	move = 0 # default
	for letter in ['O', 'X']:
		for i in possibleMoves:
			boardCopy = board[:] # cloning the board
			boardCopy[i] = letter # check for the new move results in win or not
			if isWinner(boardCopy, letter):
				move = i
				return move

	cornerOpen = []
	for i in possibleMoves:
		if i in [1, 3, 7, 9]:
			cornerOpen.append(i)
	if len(cornerOpen) > 0:
		move = selectRandom(cornerOpen)
		return move

	if 5 in possibleMoves: # center
		move = 5
		return move 


	edgeOpen = []
	for i in possibleMoves:
		if i in [2, 4, 6, 8]:
			edgeOpen.append(i)
	if len(edgeOpen) > 0:
		move = selectRandom(edgeOpen)
		
	return move

def selectRandom(checkList):
	import random
	ln = len(checkList)
	r=random.randrange(0, ln)
	return checkList[r]

def isBoardFull(board):
	if board.count(' ') > 1:
		return False
	else: return True
def main():
	print('Tic-Tac Toe Game!.')
	printBoard(board)

	while not(isBoardFull(board)):
		if not(isWinner(board, 'O')): # Computer - 0 , User - X
			playerMove()
			print('\033c') # clears the terminal 
			printBoard(board)
		else: 
			print('Computer WON!.')
			break
		if not(isWinner(board, 'X')): # Computer - 0 , User - X
			move = compMove()
			if move == 0:
				print('Game Tied!.')
			else: 
				insertLetter('O', move)
				print('\033c') # clears the terminal
				printBoard(board)
				print('Computer Played at: ', move)
		else: 
			print('You WON!.')
			break

	if isBoardFull(board) and move != 0:
		print('\033c')
		print('Game Tied!')
		

main() # start the game. 

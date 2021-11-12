import numpy as np
class gameBoard:
	def __init__(self,columns,rows):
		self.columns = columns
		self.rows  =  rows
		self.board = [[0 for i in range(columns)] for i in range(rows)]

	def getBoard(self):
		return self.board
	def printBoard(self):
		for i in range(len(self.board[0])):
			for j in range(len(self.board)):
				print(self.board[j][i], end="")
			print()
	def setBoard(self, new_board):
		self.board = new_board

	def check_straight(self,board,x,y):
		symbol = board[x][y]
		if symbol == 0:
			return False
		if(board[x][y] == symbol and board[x][y+1] == symbol and board[x][y+2] == symbol and board[x][y+3] == symbol):
			return True
		return False

	def check_diagonal(self,board,x,y):
		symbol = board[x][y]
		if (symbol == 0):
			return False
		if(board[x][y] == symbol and board[x+1][y+1] == symbol and board[x+2][y+2] == symbol and board[x+3][y+3] == symbol):
			return True
		return False

	def check(self):
		board_tbc = np.array(self.board)
		#print(board_tbc)
		for z in range(4):
			for x in range(len(board_tbc.tolist())):
				for y in range(len(board_tbc.tolist()[0])):
					if board_tbc[x][y] != '0':	
						try:
							if(self.check_diagonal(board_tbc.tolist(),x,y) or self.check_straight(board_tbc.tolist(),x,y)):
								return True
						except:
							pass
			
			board_tbc = np.rot90(board_tbc,axes=(1,0))	


		return False

class Player:
	def __init__(self,color,gameBoard):
		self.color = color;
		self.gameBoard = gameBoard
	def move(self,row):
		board = self.gameBoard.getBoard()
		for i in range(len(board[row])):
			if (board[row][i] != 0):
				board[row][i-1] = self.color
				break
			if(i == len(board[row])-1):
				board[row][i] = self.color			
		self.gameBoard.setBoard(board)
	
gameBoard = gameBoard(7,5)
player1 = Player("X",gameBoard)
player2 = Player("O",gameBoard)

i=0

while(True):
	if(i % 2 == 0):
		player1.move(int(input("Enter move:")))
	else:
		player2.move(int(input("Enter move:")))
	print(gameBoard.check())
	gameBoard.printBoard()
	i += 1



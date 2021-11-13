
class Player:
	def __init__(self,symbol,gameBoard):
		self.symbol = symbol
		self.gameBoard = gameBoard
	def move(self,row):
		board = self.gameBoard.getBoard()
		for i in range(len(board[row])):
			if (board[row][i] != " "):
				board[row][i-1] = self.symbol
				break
			if(i == len(board[row])-1):
				board[row][i] = self.symbol			
		self.gameBoard.setBoard(board)



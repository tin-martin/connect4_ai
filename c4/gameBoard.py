import numpy as np
from copy import deepcopy
class gameBoard:
	def __init__(self, board):
		self.rows = 6
		self.columns  =  7
		self.board = board
		
	def getBoard(self):
		return self.board
	def printBoard(self):
		for i in range(self.columns+2):
			print("-",end="")
		print("")
		for i in range(self.rows):
			print("|",end="")
			for j in range(self.columns):
				print(self.board[j][i], end="")
			print("|")
		for i in range(self.columns+2):
			print("-",end="")
		print("")
		
	def setBoard(self, new_board):
		self.board = new_board

	def move(self, symbol,col):
		
		board = deepcopy(self.getBoard())

		if(board[col][0] != " "):
			raise ValueError('A very specific bad thing happened.')

		for i in range(len(board[col])):
			if (board[col][i] != " "):
				board[col][i-1] = symbol
				break
			if(i == len(board[col])-1):
				board[col][i] = symbol			
		return board

	def check_straight(self,board,x,y):
		symbol = board[x][y]
		try:
			if(board[x][y] == symbol and board[x][y+1] == symbol and board[x][y+2] == symbol and board[x][y+3] == symbol):
				return True
		except:
			pass
		return False
	def check_diagonal(self,board,x,y):
		symbol = board[x][y]
		
		try:
			if(board[x][y] == symbol and board[x+1][y+1] == symbol and board[x+2][y+2] == symbol and board[x+3][y+3] == symbol):
				return True
		except:
			pass
		return False

	def check_straight2(self,board,x,y):
		symbol = board[x][y]
		try:
			if(board[x][y] == symbol and board[x+1][y] == symbol and board[x+2][y] == symbol and board[x+3][y] == symbol):
				return True
		except:
			pass
		return False
	def check_diagonal2(self,board,x,y):
		symbol = board[x][y]
		try:
			if(board[x][y] == symbol and board[x-1][y-1] == symbol and board[x-2][y-2] == symbol and board[x-3][y-3] == symbol):
				return True
		except:
			pass
		return False

	def isTerminal(self):
		board_tbc = self.board
		isTie = True

		for x in range(self.columns):
			for y in range(self.rows):
				
				if(board_tbc[x][y] == ' '):	
					isTie = False
				if(self.check_diagonal(board_tbc,x,y) or self.check_straight(board_tbc,x,y) or self.check_diagonal2(board_tbc,x,y) or self.check_straight2(board_tbc,x,y)):
					return True, board_tbc[x][y]
				
			
			
						
		if(isTie):
			return True, "TIE"
			

		return False, " "

	def get_legal_actions(self):
		legal_actions = []
		for i in range(self.columns):
			if(self.board[i][0] == " "):
				legal_actions.append(i)
		return legal_actions
"""



if __name__ == "__main__":
	state = [[" "," "," "," "," ","X"],[" "," ","X"," ","X","X"],[" "," "," ","X"," "," "],[" "," ","X","X"," "," "],[" "," ","X","X"," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]
	gb = gameBoard(state)
	print(gb.isTerminal())
	print(gb.printBoard())
"""

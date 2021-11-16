from Player import Player
from gameBoard import gameBoard
if __name__ == '__main__':	
	gameBoard = gameBoard(7,6)
	player1 = Player("X",gameBoard)
	player2 = Player("O",gameBoard)	
	i=0
	while(True):
		if(i % 2 == 0):
			gameBoard.board = gameBoard.move("O", int(input("Enter move:")))
		else:
			gameBoard.board = gameBoard.move("X", int(input("Enter move:")))

		
		gameBoard.printBoard()
		isFinished, winner = gameBoard.isTerminal()

		if(isFinished):
			print("The winner is... ", winner)
		i += 1

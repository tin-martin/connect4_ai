from Player import Player
from gameBoard import gameBoard

if __name__ == '__main__':	
	gameBoard = gameBoard(7,6)
	i=0
	while(True):
		if(i % 2 == 0):
			while(True):
				try:
					gameBoard.board = gameBoard.move("O", int(input("Enter move:")))
					break
				except:
					pass
		else:
			while(True):
				try:
					gameBoard.board = gameBoard.move("X", int(input("Enter move:")))
					break
				except:
					pass
			
		print(gameBoard.board)
		gameBoard.printBoard()
		isFinished, winner = gameBoard.isTerminal()

		if(isFinished):
			if(winner == "TIE"):
				print("issa tie")
			else:
				print("The winner is... ", winner)
			break
		i += 1


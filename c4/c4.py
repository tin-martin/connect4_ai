from Player import Player
from gameBoard import gameBoard

if __name__ == '__main__':	
	state =[[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
	gameBoard = gameBoard(state)
	i=0
	while(True):
		if(i % 2 == 0):
			while(True):
				try:
					gameBoard.board = gameBoard.move(2, int(input("Enter move:")))
					break
				except:
					pass
		else:
			while(True):
				try:
					gameBoard.board = gameBoard.move(1, int(input("Enter move:")))
					break
				except:
					pass
			
		gameBoard.printBoard()
		isFinished, winner = gameBoard.isTerminal()

		if(isFinished):
			if(winner == "TIE"):
				print("issa tie")
			else:
				print("The winner is... ", winner)
			break
		i += 1


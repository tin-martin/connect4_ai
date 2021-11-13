from Player import Player
from gameBoard import gameBoard
if __name__ == '__main__':	
	gameBoard = gameBoard(7,5)
	player1 = Player("X",gameBoard)
	player2 = Player("O",gameBoard)	
	i=0
	while(True):
		if(i % 2 == 0):
			player1.move(int(input("Enter move:")))
		else:
			player2.move(int(input("Enter move:")))

		gameBoard.printBoard()
		if(gameBoard.check("X") == "win"):
			print("And the winner is... X")
		elif(gameBoard.check("O") == "win"):
			print("And the winner is... O")
		i += 1

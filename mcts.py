import numpy as np
import random
from c4 import gameBoard, Player
from copy import deepcopy
class mctsNode:
    def __init__(self, parent,parent_action, symbol):

      self.gameBoard = gameBoard.gameBoard(6,7)
      self.symbol = symbol

      if not (parent == None):
        self.parent = parent
        self.parent_action = parent_action
        self.s = self.parent.si

        
        self.gameBoard.setBoard(parent.gameBoard.move(self.parent.symbol,self.parent_action))
      else:
        
        self.s = 1 #what is the # of parent node simulations for a root node


      self.state = self.gameBoard.getBoard()

      self.childs = []
      self.untried_actions = self.legal_actions()
      self.legal_actions = self.legal_actions()
      
      self.w = 0
      self.si = 0
      


    def legal_actions(self):    #verifiably pog
    	legal_actions = []
    	for i in range(6):
    		if(self.state[i][0] == " "):
    			legal_actions.append(i)
    	return legal_actions

    def untried_actions(self):
    	possible_actions = self.legal_actions()
    	for child in self.childs:
    		if(child.parent_action in self.untried_actions):
    			self.untried_actions.remove(child.parent_action)

    def ucb1(self,node):
    	c = math.sqrt(2)
    	return (node.wi/node.si) + c*(math.log(node.s)/node.si)

    def selection(self):
      actions = self.legal_actions

      if(len(self.untried_actions) > 0):
        return random.choice(self.untried_actions)
      _max = 0

      counter=0
      for i in range(len(self.childs)):
        counter = i
        if (self.ucb1(self.childs[i]) > _max):
          _max = self.ucb1(self.childs[i])

      child = self.childs[counter]
      child.selection()

    #gets action from selection function
    def expansion(self,action):

      if (self.symbol == "X"):
        new_symbol = "O"
      else:
        new_symbol = "X"

      new_child = mctsNode(self,action,new_symbol)

      self.childs.append(new_child)
      return new_child
    #gets child from expansioin
    def simulation(self,node):
      temp_node = deepcopy(node) 

      isFinished, winner = node.gameBoard.isTerminal()
      temp_symbol = temp_node.symbol
      while not(isFinished):
        action = random.choice(temp_node.legal_actions)
        temp_gameBoard = temp_node.gameBoard.move(temp_symbol,action) 
        temp_node.gameBoard.setBoard(temp_gameBoard)
        temp_node.gameBoard.printBoard()
        isFinished, winner = temp_node.gameBoard.isTerminal()
        if(temp_symbol == "X"):
          temp_symbol = "O"
        else:
          temp_symbol = "X"
      return winner

    def backpropogation(self):
      for ()


def mcts():
  root = mctsNode(None,None,"X")
  a = root.expansion(root.selection())
  print(a.simulation(a))
if __name__ == '__main__':
  mcts()

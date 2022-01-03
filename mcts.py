import numpy as np
import random
from c4 import gameBoard, Player
from copy import deepcopy
import math
class mctsNode:
    def __init__(self, parent,parent_action, symbol):

      self.gameBoard = gameBoard.gameBoard(6,7)
      self.symbol = symbol

      if (parent != None):
        self.parent = parent
        self.parent_action = parent_action
        self.s = self.parent.si

        
        self.gameBoard.setBoard(parent.gameBoard.move(self.symbol,self.parent_action))
      else:
        self.si = 0
        self.s = 0 #what is the # of parent node simulations for a root node

      self.state = self.gameBoard.getBoard()

      self.childs = []
      self.untried_actions = deepcopy(self.legal_actions())
      self.legal_actions = deepcopy(self.legal_actions())
      
      self.w = 0
      
    def printBoard(self):
      for i in range(self.rows+2):
        print("-",end="")
      print("")
      for i in range(len(self.board[0])):
        print("|",end="")
        for j in range(len(self.board)):
          print(self.board[j][i], end="")
        print("|")
      for i in range(self.rows+2):
        print("-",end="")
      print("")


    def legal_actions(self):    #verifiably pog
    	legal_actions = []
    	for i in range(6):
    		if(self.state[i][0] == " "):
    			legal_actions.append(i)#chicken finngers1231231231231223223
    	return legal_actions

    def untried_actions(self):
    	possible_actions = self.legal_actions()
    	for child in self.childs:
    		if(child.parent_action in self.untried_actions):
    			self.untried_actions.remove(child.parent_action)

    def ucb1(self,node):
      c = math.sqrt(2)
      try:
        return (node.w/node.si) + c*(math.log(node.s)/node.si)
      except:
        return 0
    	

    def selection(self):
      actions = self.legal_actions

      if(len(self.untried_actions) > 0):
        temp_action = random.choice(self.untried_actions)
        self.untried_actions.remove(temp_action)
        return self, temp_action
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
      return winner, node

def backprop(expanded_node,winner):
  try:
    while(True):
      if(expanded_node.symbol == winner):
        expanded_node.si += 1
 
      expanded_node = expanded_node.parent
  except:
    pass

def bestPlay(self):
  pass


def mcts():
  root = mctsNode(None,None,"O")
  for i in range(5):
    parent_tbe, action = root.selection()
    a = parent_tbe.expansion(action)

    winner, node = a.simulation(a)
    backprop(a,winner)
 # print(root.si)
  root.gameBoard.printBoard()
  for child in root.childs:

    print(child.s)
    child.gameBoard.printBoard()


if __name__ == '__main__':
  mcts()
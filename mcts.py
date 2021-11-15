import numpy as np
import random
from c4 import gameBoard, Player
from copy import deepcopy
class mctsNode:
    def __init__(self, state, parent,parent_action, symbol):
      
    	self.parent = parent
      self.parent_action = parent_action
      self.symbol = symbol

      self.gameBoard = gameBoard.gameBoard(6,7)
      self.gameBoard.setBoard = parent.gameBoard.move(self.symbol,self.parent_action)


    	self.childs = []
    	
    	self.legal_actions = self.legal_actions()
    	self.untried_actions = self.legal_actions()
    	self.w = 0
    	self.si = 0
    	self.s = self.parent.si



    def legal_actions(self):    #verifiably pog
    	gameBoard = self.state
    	legal_actions = []
    	for i in range(6):
    		if(gameBoard[i][0] == " "):
    			legal_actions.add(i)
    	return legal_actions

    def untried_actions(self):
    	possible_actions = self.legal_actions()
    	for child in self.childs:
    		if(child.parent_action in self.untried_actions):
    			self.untred_actions.remove(child.parent_action)

    def ucb1(self,node):
    	c = math.sqrt(2)
    	return (node.wi/node.si) + c*(math.log(node.s)/node.si)


    def selection(self):
      actions = self.legal_actions
      for child in self.childs:
        if(len(self.untried_actions > 0)):
          return random.choice(self.untried_actions)
      _max = 0
      
      for i in range(len(self.childs)):
        if (self.ucb1(self.childs[i]) > _max):
          _max = self.ucb1(self.childs[i])
          child = self.child[i]
      selection(child)

    #gets action from selection function
    def expansion(self,action):

      (self, state, parent,parent_action, symbol):

      if (self.symbol == "X"):
        new_symbol = "O"
      else:
        new_symbol = "X"

      new_child = mctsNode(self.gameBoard.move(self.symbol,action),self,action,new_symbol)
      self.childs.add(new_child)
    	return new_child


    #gets child from expansioin
    def simulation(self,node):
      temp_node = deepcopy(node) 
      isFinished, winner = node.gameBoard.isTerminal()
      while not(isFinished):
        action = random.choice(temp_node.possible_actions)
        temp_gameBoard = temp_gameBoard.move(temp_node.symbol,action) 
        isFinished, winner = node.gameBoard.isTerminal()
      return winner

      

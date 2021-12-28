from os import fdopen
from typing import DefaultDict
import numpy as np
import random
from numpy.lib.function_base import _diff_dispatcher, diff

from numpy.testing._private.utils import _assert_valid_refcount
from c4 import gameBoard
from copy import deepcopy
import math

class Node:
    def __init__(self, gameBoard, parent: object = None, symbol: str = "X"):
        self.gb = gameBoard
    
        self.state = deepcopy(self.gb.board)

        self.rows, self.columns = 6,7

        self.parent = parent
        self.childs = []

        self.legal_actions = self.get_legal_actions()
        self.untried_actions = self.get_legal_actions()

        self.wins = 0
        self.visits = 0
        if(self.parent == None):
            self.visits  = 1
        else:
            self.ucb1 = self.calculate_ucb1()

        self.symbol = symbol

        self.action = None
    
    def get_legal_actions(self):
        legal_actions = []
        for i in range(self.rows):
            if(self.state[i][0] == " "):
                legal_actions.append(i)
        self.legal_actions = legal_actions
        return legal_actions

    def calculate_ucb1(self):
        if self.visits == 0:
            return 0
        ####################################
        if self.parent.parent == None:
            self.parent.visits = 0
            for child in self.parent.childs:
                self.parent.visits += child.visits
        ########################################

        return self.wins/self.visits + np.sqrt(2)*np.sqrt(np.log(self.parent.visits)/self.visits)

    def select(self):
        foo = lambda x:  x.calculate_ucb1()
        return sorted(self.childs,key=foo)[-1]
    



    def expand(self):
        temp_action = random.choice(self.untried_actions)
       
        self.untried_actions.remove(temp_action)

        if(self.symbol == "X"):
            new_symbol = "O"
        else:
            new_symbol = "X"

        new_state = self.gb.move(new_symbol,temp_action)

        new_gb = gameBoard.gameBoard(new_state)
        child = Node(new_gb,self,new_symbol)
        ###############################
        child.action = temp_action
        ###############################
        self.childs.append(child)
        
        return child

    def simulate(self):

        gb = deepcopy(self.gb)
        isFinished, winner = gb.isTerminal()
        symbol = self.symbol
        while not(isFinished):
            if(symbol == "X"):
                symbol = "O"
            else:
                symbol = "X"

            gb.board = gb.move(symbol,random.choice(gb.get_legal_actions()))

            isFinished, winner = gb.isTerminal()
            

        return winner

    def update(self, winner):
        if(self.symbol == winner):
            self.wins += 1
        self.visits += 1
    
    def backprop(self,winner):
        node = self
        while node.parent is not None:
            node.update(winner)
            node.calculate_ucb1()
            node = node.parent

if __name__ == "__main__":
    state = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    root_gb = gameBoard.gameBoard(board=state)
    root_node = Node(gameBoard=root_gb)
    
    current_node = root_node
    for i in range(10000000):
        if(len(current_node.untried_actions) == 0):
            current_node = current_node.select()  
        else:
            current_node = current_node.expand()

            winner = current_node.simulate()
            
            current_node.backprop(winner)
            current_node.gb.printBoard()
            
            current_node = root_node
    
    def check_childs(node,state,the_node):
        for child in node.childs:
            if(child.state == state):
                the_node = child
        for child in node.childs:
            check_childs(child,state,the_node)

    def best_move(state,symbol):
        the_node = None
        check_childs(root_node,state,the_node)

        foo = lambda x:  x.visits
        node = sorted(the_node.childs,key=foo)[-1]
        return node.action
        
        

    oState = state = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    gb = gameBoard.gameBoard(state)

    symbol = "X"
    while(True):
        symbol = "O"
        gb.move(symbol,best_move(gb.board,symbol))
        gb.printBoard()
        

            
            
            #check tempnnode childs
           # check all childs of tempnode childs
           # check all childs of that

            



        #find state in tree
        #search childs, get one with max visits 
        #TOO EEZZZ

            
            
            
        
        
       
    
    #state, parent, symbol

#9:58

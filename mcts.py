from os import fdopen
from typing import DefaultDict
import numpy as np
import random
from numpy.lib.function_base import _diff_dispatcher, diff

from numpy.testing._private.utils import _assert_valid_refcount
from c4 import gameBoard
from copy import deepcopy
import math
import pickle
import pyautogui
import sys
import time

start_time = time.time()

class Node:
    def __init__(self, gameBoard, parent: object = None, symbol: str = 1,exploration_parameter: int=math.sqrt(2)):
        self.gb = gameBoard
    
        self.state = deepcopy(self.gb.board)

        self.rows, self.columns = 6,7

        self.parent = parent
        self.childs = []

        self.legal_actions = self.gb.get_legal_actions()
        self.untried_actions = self.gb.get_legal_actions()
        self.wins = 0
        self.visits = 0
        self.ucb1 = self.calculate_ucb1()

        self.symbol = symbol

        self.action = None
        self.exploration_parameter = exploration_parameter

    def calculate_ucb1(self):
        if(self.visits == 0):
            return 0
        ####aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
        if(self.parent.parent == None):
            self.parent.visits = 0
            for child in self.parent.childs:
                self.parent.visits += child.visits
        ########################################a
        #print(self.wins/self.visits + np.sqrt(2)*np.sqrt(np.log(self.parent.visits)/self.visits))
        return self.wins/self.visits + np.sqrt(self.exploration_parameter)*np.sqrt(np.log(self.parent.visits)/self.visits)

    def select(self):
        foo = lambda x:  x.ucb1
        return sorted(self.childs,key=foo)[-1]

    def expand(self):
        temp_action = random.choice(self.untried_actions)
       
        self.untried_actions.remove(temp_action)

        if(self.symbol == 1):
            new_symbol = 2
        else:
            new_symbol = 1

        new_state = self.gb.move(new_symbol,temp_action)

        new_gb = gameBoard.gameBoard(new_state)
        child = Node(new_gb,self,new_symbol,exploration_parameter = self.exploration_parameter)
        ###############################
        child.action = temp_action
        ###############################
        self.childs.append(child)
        
        return child

    def simulate(self):

        gb = deepcopy(self.gb)
        isFinished, winner = gb.isTerminal()
        symbol = deepcopy(self.symbol)
        while not(isFinished):
            if(symbol == 1):
                symbol = 2
            else:
                symbol = 1
                
            gb.board = gb.move(symbol,random.choice(gb.get_legal_actions()))

            isFinished, winner = gb.isTerminal()
        return winner

    def update(self, winner):
        if(self.symbol == winner):
            self.wins += 1
        if(self.symbol == "TIE"):
            self.wins += 0.5
        self.visits += 1
    
    def backprop(self,winner):
        node = self
        while node.parent is not None:
            node.update(winner)
            node.ucb1 = node.calculate_ucb1()
            node = node.parent

def find_best_move(state,iterations=10000,max_depth=5,exploration_parameter=math.sqrt(2),symbol=1):
    root_gb = gameBoard.gameBoard(board=state)
    root_node = Node(gameBoard=root_gb,exploration_parameter=exploration_parameter,symbol=symbol) 
    current_node = root_node
    depth = 0
    counter = 0
    for i in range(iterations):
        
        print(i)
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')
        earlyQuit = False
        while(len(current_node.untried_actions) == 0):
            isFinished,winner = current_node.gb.isTerminal()
            if(isFinished):
                current_node.backprop(winner)
                current_node = root_node
                depth = 0
                earlyQuit = True
                break
            else:
                current_node = current_node.select()  
                depth += 1
                if(depth > max_depth):
                    earlyQuit = True
                    break
        if(earlyQuit):
            winner = current_node.simulate()
            current_node.backprop(winner)
            current_node = root_node
            depth = 0 
            continue
        current_node = current_node.expand()
        counter+=1

        winner = current_node.simulate()
        
        current_node.backprop(winner)
      
        current_node = root_node
        depth = 0

    

    foo = lambda x:  x.visits
    a = root_node.childs
    action = sorted(a,key=foo)[-1].action
    return action

if __name__ == "__main__":
    state = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
           
        

   
    gb = gameBoard.gameBoard(state)

    symbol = 1

    isFinished, winner = gb.isTerminal()

    gb.printBoard()
    player_goes_first = input("Do you want to go first? (Y for yes, N for no) ")

    if(player_goes_first == "N"):
        while not(isFinished):
            if(symbol == 1):
                symbol = 2 
                best_move = find_best_move(gb.board,10000,4,exploration_parameter=math.sqrt(2)-0.001)
                gb.board = gb.move(symbol,best_move)
                print("Computer move: " + str(best_move))
            else:
                symbol = 1    
                gb.board = gb.move(symbol,int(input("Enter move: ")))
            gb.printBoard()
            
            isFinished, winner = gb.isTerminal()
    else:
        while not(isFinished):
            if(symbol == 2):
                symbol = 1 
                best_move = find_best_move(gb.board,10000,4,exploration_parameter=math.sqrt(2)-0.001,symbol=2)
                gb.board = gb.move(symbol,best_move)
                print("Computer move: " + str(best_move))
            else:
                symbol = 2    #X
                #gb.board = gb.move(symbol,find_best_move(gb.board,100000,42,exploration_parameter=math.sqrt(2)))
                gb.board = gb.move(symbol,int(input("Enter move: ")))
            gb.printBoard()
            
            isFinished, winner = gb.isTerminal()
    if(winner == "TIE"):
        print("IT'S A TIE!")
    elif((player_goes_first != "N" and winner == 2) or (player_goes_first == "N" and winner == 1)):
        print("PLAYER WINS!")
    elif((player_goes_first != "N" and winner == 1) or (player_goes_first == "N" and winner == 2)):
        print("COMPUTER WINS!")
    

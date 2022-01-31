
# import the opencv library
import cv2
import cv
import numpy as np
import time 
from c4 import gameBoard
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

import time
import mcts_v2
# define a video capture object
vid = cv2.VideoCapture(0)
def increase_brightness(img, value=0):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img


state = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0]]
root_gb = gameBoard.gameBoard(board=state)
root_node = mcts_v2.Node(gameBoard=root_gb)

current_node = root_node
rects = []

while(True):

    ret, frame = vid.read()
    cv2.imshow('frame', frame)

    
    key = cv2.waitKey(1)
    if key == 27:
        break


while(True):

    ret, frame = vid.read()

    frame,rects =  cv.setgrid(frame)

    cv2.imshow('frame', frame)

    
    key = cv2.waitKey(0)
    if key == 27:#if ESC is pressed, exit loop
        break


player_starts_first = input("Do you want to start first? (Y for yes, N for no)")

isTerminal = False

if(player_starts_first == "N"):
    computer_symbol = 2
    player_symbol = 1
    
    ret, frame = vid.read()
    state,frame =  cv.fill(frame,rects,6,7)
    gb = gameBoard.gameBoard(state)
    isTerminal, winner = gb.isTerminal()
    if(isTerminal):
        gb.printBoard()
        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (50, 50)
        fontScale = 1
        color = (255, 0, 0)
        thickness = 2
        text = ""
        if(winner == player_symbol):
            text = "PLAYER WINS!"
        elif(winner == computer_symbol):
            text = "AI WINS!"
        else:
            text = "ITS A TIE!"
        frame = cv2.putText(frame, text, org, font, fontScale, color, thickness, cv2.LINE_AA)
        cv2.imshow('frame',frame)
        cv2.waitKey(0)

    cv2.imshow('frame', frame)
    cv2.waitKey(0)

else:
    
    player_symbol = 2
    computer_symbol = 1

    ret, frame = vid.read()
    state,frame =  cv.fill(frame,rects,6,7)
    gb = gameBoard.gameBoard(state)
    isTerminal, winner = gb.isTerminal()
    gb.printBoard()
    if(isTerminal):
        print("SDFDS")
        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (50, 50)
        fontScale = 1
        color = (255, 0, 0)
        thickness = 2
        text = ""
        if(winner == player_symbol):
            text = "PLAYER WINS!"
        elif(winner == computer_symbol):
            text = "AI WINS!"
        else:
            text = "ITS A TIE!"
        frame = cv2.putText(frame, text, org, font, fontScale, color, thickness, cv2.LINE_AA)
        cv2.imshow('frame',frame)
        cv2.waitKey(0)
        print("SDFDS")
    cv2.imshow('frame', frame)
    cv2.waitKey(0)



while not(isTerminal):
    ret, frame = vid.read()
    state,frame =  cv.fill(frame,rects,6,7)
    gb = gameBoard.gameBoard(state)
    isTerminal, winner = gb.isTerminal()
    gb.printBoard()

    cv2.imshow('frame', frame)
    cv2.waitKey(0)
    if(isTerminal):
        break
    best_move = mcts_v2.find_best_move(state,1000,50,exploration_parameter=math.sqrt(2),symbol=player_symbol)
    print("Best Move: ",best_move)
    temp_state = gb.move(computer_symbol+10,best_move)
    state = gb.move(computer_symbol,best_move)
    
    gb.board = state
    frame =  cv.fill_extra(frame,rects,6,7,temp_state)
    
    isTerminal, winner = gb.isTerminal()
    
    if(isTerminal):
        print("SDFDS")
        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (50, 50)
        fontScale = 1
        color = (255, 0, 0)
        thickness = 2
        text = ""
        if(winner == player_symbol):
            text = "PLAYER WINS!"
        elif(winner == computer_symbol):
            text = "AI WINS!"
        else:
            text = "ITS A TIE!"
        frame = cv2.putText(frame, text, org, font, fontScale, color, thickness, cv2.LINE_AA)
        cv2.imshow('frame',frame)
        cv2.waitKey(0)
        print("SDFDS")
        break
    cv2.imshow('frame', frame)
    cv2.waitKey(0)



  
vid.release()
cv2.destroyAllWindows()
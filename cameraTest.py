
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
vid = cv2.VideoCapture(3)
"""

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
for i in range(50000000):
#for i in range(10000):
    
    if(len(current_node.untried_actions) == 0):
        isFinished,winner = current_node.gb.isTerminal()
        if(isFinished):
            current_node.backprop(winner)
            current_node.gb.printBoard()
            current_node = root_node
        else:
            current_node = current_node.select()  
        
    else:    
        current_node = current_node.expand()

        winner = current_node.simulate()
        
        current_node.backprop(winner)
        current_node.gb.printBoard()
        
        current_node = root_node
        print(i)
    



def check_childs(node,state,the_node):
    for child in node.childs:
        if(the_node != None):
            break
        if(child.state == state):
            the_node = child
    
    if(the_node == None):
        for child in node.childs:
            if(the_node != None):
                break
            check_childs(child,state,the_node)

def best_move(state,symbol):
    the_node = None
    if(root_node.state == state):
        the_node = root_node
    else:
        check_childs(root_node,state,the_node)

    foo = lambda x:  x.visits
    action = sorted(the_node.childs,key=foo)[-1].action
    return action
    
    

"""







rects = []










while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
   # frame = increase_brightness(frame,30)

    
   
    # Display the resulting frame
    cv2.imshow("", frame)
    
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    
    key = cv2.waitKey(1)
    if key == 27:#if ESC is pressed, exit loop
        break


while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
   # frame = increase_brightness(frame,30)

    frame,rects =  cv.setgrid(frame)

   
    # Display the resulting frame
    cv2.imshow("", frame)
    
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    
    
    key = cv2.waitKey(0)
    if key == 27:#if ESC is pressed, exit loop
        break
 

while(True):  
    ret, frame = vid.read()
    board,frame =  cv.fill(frame,rects,6,7)
    gb = gameBoard.gameBoard(board)
   
    gb.printBoard()
    cv2.imshow('frame', frame)
    cv2.waitKey(0)
    print("Best Move: ",mcts_v2.find_best_move(board,1000,4))
    
    


vid.release()
# Destroy all the windows
cv2.destroyAllWindows()

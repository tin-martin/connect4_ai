
# import the opencv library
import cv2
import cv
import numpy as np
import time 
from c4 import gameBoard
# define a video capture object
vid = cv2.VideoCapture(2)
def increase_brightness(img, value=0):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img


rects = []
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
   # frame = increase_brightness(frame,30)

    
   
    # Display the resulting frame
    cv2.imshow('frame', frame)
    
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
    cv2.imshow('frame', frame)
    
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    
    
    key = cv2.waitKey(0)
    if key == 27:#if ESC is pressed, exit loop
        break

while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
   # frame = increase_brightness(frame,30)

    board,frame =  cv.fill(frame,rects,6,7)
    gb = gameBoard.gameBoard(board)
    gb.printBoard()
   
    # Display the resulting frame
    cv2.imshow('frame', frame)
    
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    
    
    key = cv2.waitKey(5000)
    if key == 27:#if ESC is pressed, exit loop
        break
    

  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
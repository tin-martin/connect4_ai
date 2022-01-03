
from PIL import Image
import cv2
import imutils
print(cv2.__version__)
import numpy as np
import matplotlib.pyplot as plt
import math
image = cv2.imread('/Users/martintin/Downloads/IMG_0857.JPG')
image = cv2.imread('/Users/martintin/Downloads/IMG_0862.JPG')

#image = cv2.imread('/Users/martintin/Desktop/Google Downloads/550px-nowatermark-Win-at-Connect-4-Step-9-Version-2.jpeg')
#image = cv2.imread('/Users/martintin/Desktop/Screen Shot 2021-12-31 at 11.02.42 PM.png')


new_width = 500 # Resize
img_h,img_w,_ = image.shape
scale = new_width / img_w
img_w = int(img_w * scale)
img_h = int(img_h * scale)
image = cv2.resize(image, (img_w,img_h), interpolation = cv2.INTER_AREA)
copy = image.copy()
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.bilateralFilter(image,15,80,80) 
font = cv2.FONT_HERSHEY_COMPLEX

image = cv2.fastNlMeansDenoising(image,10,7,21)

kernel = np.ones((5,5),np.uint8)
image = cv2.erode(image,kernel,iterations = 1)

edges = cv2.Canny(image, 65,120) 

cv2.imshow("output", edges)
cv2.waitKey(0)

uImg = image.copy()

_, threshold = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

cnts, hierarchy = cv2.findContours(threshold
, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

org = (50, 50)
  
# fontScale
fontScale = 1
   
# Blue color in BGR
color = (255, 0, 0)
  
# Line thickness of 2 px
thickness = 2
   
# Using cv2.putText() method

rects = []
for contour in cnts:
    cnt = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True) 
    if(len(cnt) == 4 or len(cnt) == 3):
        cv2.drawContours(image, [cnt], 0, (0), 1)
        x = cnt.ravel()[0]
        y = cnt.ravel()[1]
        image = cv2.putText(image, str(len(cnt)), (x,y), font, 
                    fontScale, color, thickness, cv2.LINE_AA)	

        cv2.imshow("",image)
        cv2.waitKey(0)
    


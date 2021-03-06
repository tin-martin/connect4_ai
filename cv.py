
from PIL import Image
import cv2
import imutils
print(cv2.__version__)
import numpy as np
import matplotlib.pyplot as plt
import math,time
def setgrid(image):
    rects = []
    try:
        new_width = 500 # Resize
        img_h,img_w,_ = image.shape
        scale = new_width / img_w
        img_w = int(img_w * scale)
        img_h = int(img_h * scale)
        image = cv2.resize(image, (img_w,img_h), interpolation = cv2.INTER_AREA)
        cv2.imshow("frame",image)
        cv2.waitKey(0)
        copy = image.copy()

        image = cv2.bilateralFilter(image,10,190,190) 
       # cv2.imshow("frame",image)
       # cv2.waitKey(0)

        image = cv2.fastNlMeansDenoising(image,10,7,21)
      #  cv2.imshow("frame",image)
      #  cv2.waitKey(0)


        edges = cv2.Canny(image, 45,120)
      #  cv2.imshow("frame",edges)
      #  cv2.waitKey(0)
        uImg = image.copy()

        contours, hierarchy = cv2.findContours(edges
        , cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        font = cv2.FONT_HERSHEY_COMPLEX 

        good_contours = []
        copy1 = image.copy()
        for contour in contours:
            cv2.drawContours(copy1, contour, -1, (0,255,0), 1)
     #   cv2.imshow("frame",copy1)
     #   cv2.waitKey(0)

        copy1 = image.copy()
        for contour in contours:
            cnt = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True) 
            cv2.drawContours(copy1, [cnt], -1, (0, 255, 0), 1)
      #  cv2.imshow("frame",copy1)
      #  cv2.waitKey(0)

        copy1 = image.copy()
        for contour in contours:
            cnt = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True) 
            x,y,w,h = cv2.boundingRect(cnt)
            area = w*h
            d=w
            c = math.pi*d
            if(len(cnt) >= 8 and 100*(w/h) > 80 and 100*(h/w) > 80 and c >= cv2.arcLength(cnt,True)-15 and c <= cv2.arcLength(cnt,True)+15         ):    
                rects.append([x,y,w,h])
                good_contours.append([cnt])
                cv2.drawContours(copy1, [cnt], -1, (0, 255, 0), 1)

      #  cv2.imshow("frame",copy1)
     #   cv2.waitKey(0)
        
        copy1 = image.copy()
        toDel = []

        avg_area = int(math.trunc(sum([r[2]*r[3] for r in rects])/len(rects)))
        best_contours = []
        for rect,good_contour in zip(rects,good_contours):
            x,y,w,h = rect
            a = w*h
            if (a >= (avg_area-200) and a <= (avg_area+200)):
                
                cv2.rectangle(copy1,(x,y),(x+w,y+h),(0,255,0),2)
                cv2.drawContours(copy1, [cnt], -1, (0, 255, 0), 1)
                best_contours.append(cnt)
            else: 
                toDel.append(rect)
        good_contours = best_contours
        
        cv2.imshow("frame",copy1)
        cv2.waitKey(0)
      
        for r in toDel:
            rects.remove(r)
      
        copy2 = image.copy()

        avg_width = sum([r[2] for r in rects])/len(rects)
        avg_height = sum([r[3] for r in rects])/len(rects)
        cv2.imshow("frame",copy1)
        cv2.waitKey(0)
        
            #make grid
        cols,rows = 7,6
    
        foo = lambda x : x[0]
        rects.sort(key=foo)
        max_x = rects[-1][0]
        min_x = rects[0][0]
        foo = lambda x : x[1]
        rects.sort(key=foo)
        max_y = rects[-1][1]
        min_y = rects[0][1]

        width = max_x - min_x
        height = max_y - min_y

        spacing_x = width/(cols-1)
        spacing_y = height/(rows-1)

        radius = int((avg_width+avg_height)/4)

        for row in range(rows):
            for col in range(cols):
                
                x = int(min_x+spacing_x*(col)+radius)
                y = int(min_y+spacing_y*(row)+radius)
                
                cv2.circle(image,(x,y),radius+2,(0,0,0),1)
    except:
        pass
    return image,rects

def fill_extra(image, rects, rows, cols, board):
    new_width = 500 # Resize
    img_h,img_w,_ = image.shape
    scale = new_width / img_w
    img_w = int(img_w * scale)
    img_h = int(img_h * scale)
    image = cv2.resize(image, (img_w,img_h), interpolation = cv2.INTER_AREA)
    avg_area = int(math.trunc(sum([r[2]*r[3] for r in rects])/len(rects)))

        
    for rect in rects:
        x,y,w,h = rect
        a = w*h
        #cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
        # cv2.drawContours(image, [cnt], 0, (0), 1)
        
    avg_width = sum([r[2] for r in rects])/len(rects)
    avg_height = sum([r[3] for r in rects])/len(rects)

    foo = lambda x : x[0]
    rects.sort(key=foo)
    max_x = rects[-1][0]
    min_x = rects[0][0]
    foo = lambda x : x[1]
    rects.sort(key=foo)
    max_y = rects[-1][1]
    min_y = rects[0][1]

    width = max_x - min_x
    height = max_y - min_y

    spacing_x = width/(cols-1)
    spacing_y = height/(rows-1)

    radius = int((avg_width+avg_height)/4)

    for row in range(rows):
        for col in range(cols):
            
            x = int(min_x+spacing_x*(col)+radius)
            y = int(min_y+spacing_y*(row)+radius)
            
           # cv2.circle(image,(x,y),radius+2,1,1)

    copy = image.copy()
    height,width,depth = copy.shape

    for row in range(rows):
        for col in range(cols): 
            x = int(min_x+spacing_x*(col)+radius)
            y = int(min_y+spacing_y*(row)+radius)
            
        
            if(board[col][row] == 1):
                cv2.circle(copy,(x,y),radius,(0,0,255),-1)
            elif(board[col][row] == 2):
                cv2.circle(copy,(x,y),radius,(0,255,255),-1)
            elif(board[col][row] == 11):
                cv2.circle(copy,(x,y),radius,(0,0,255),-1)
                cv2.circle(copy,(x,y),radius,(255,0,0),2)
            elif(board[col][row] == 12):
                cv2.circle(copy,(x,y),radius,(0,255,255),-1)
                cv2.circle(copy,(x,y),radius,(255,0,0),2)
                
            else:
                pass
                #cv2.circle(copy,(x,y),radius,(0,0,0),1)

    return copy

def fill(image,rects,rows,cols):
    board = [[0 for i in range(rows)] for j in range(cols)]
    new_width = 500 # Resize
    img_h,img_w,_ = image.shape
    scale = new_width / img_w
    img_w = int(img_w * scale)
    img_h = int(img_h * scale)
    image = cv2.resize(image, (img_w,img_h), interpolation = cv2.INTER_AREA)
    avg_area = int(math.trunc(sum([r[2]*r[3] for r in rects])/len(rects)))

        
    for rect in rects:
        x,y,w,h = rect
        a = w*h
        #cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
        # cv2.drawContours(image, [cnt], 0, (0), 1)
        
    avg_width = sum([r[2] for r in rects])/len(rects)
    avg_height = sum([r[3] for r in rects])/len(rects)

    foo = lambda x : x[0]
    rects.sort(key=foo)
    max_x = rects[-1][0]
    min_x = rects[0][0]
    foo = lambda x : x[1]
    rects.sort(key=foo)
    max_y = rects[-1][1]
    min_y = rects[0][1]

    width = max_x - min_x
    height = max_y - min_y

    spacing_x = width/(cols-1)
    spacing_y = height/(rows-1)

    radius = int((avg_width+avg_height)/4)

    for row in range(rows):
        for col in range(cols):
            
            x = int(min_x+spacing_x*(col)+radius)
            y = int(min_y+spacing_y*(row)+radius)
            
            cv2.circle(image,(x,y),radius+2,1,1)

    copy = image.copy()
    height,width,depth = copy.shape

    circle_img = np.zeros((height,width), np.uint8)

    hsv = cv2.cvtColor(copy, cv2.COLOR_BGR2HSV)


    for row in range(rows):
        for col in range(cols):
            
            x = int(min_x+spacing_x*(col)+radius)
            y = int(min_y+spacing_y*(row)+radius)
            
            cv2.circle(circle_img,(x,y),radius+2,1,-1)

            red_lower = np.array([0, 50, 20])
            red_upper = np.array([10, 255, 255])

            red_lower2 = np.array([170, 70, 50])
            red_upper2 = np.array([180, 255, 255])
            #https://stackoverflow.com/questions/32522989/opencv-better-detection-of-red-color
          
            mask = cv2.inRange(hsv, red_lower, red_upper)
            mask2 = cv2.inRange(hsv,red_lower2,red_upper2)
            mask = cv2.bitwise_or(mask,mask2)
            mask = cv2.bitwise_and(mask,circle_img)
            thingy = cv2.bitwise_and(hsv,hsv,mask=mask)

            num_red = cv2.countNonZero(mask)
            percent_red = (num_red/(math.pi*radius*2))*100
          
          ##################################################
            
            yellow_lower = np.array([22, 93, 0])
            yellow_upper = np.array([45, 255, 255])
#https://stackoverflow.com/questions/9179189/detect-yellow-color-in-opencv/19488733

            circle_img = np.zeros((height,width), np.uint8)
            cv2.circle(circle_img,(x,y),radius,1,-1)
            mask1 = cv2.inRange(hsv, yellow_lower, yellow_upper)
            mask1 = cv2.bitwise_and(mask1,circle_img)
            thingy1 = cv2.bitwise_and(hsv,hsv,mask=mask1)

            num_yellow = cv2.countNonZero(mask1)
            percent_yellow = (num_yellow/(math.pi*radius*2))*100

            if(percent_red >= 80):
                board[col][row] = 1
                cv2.circle(copy,(x,y),radius,(0,0,255),-1)
            elif(percent_yellow >= 8):
                board[col][row] = 2
                cv2.circle(copy,(x,y),radius,(0,255,255),-1)
            else:
                cv2.circle(copy,(x,y),radius,(0,0,0),1)

            circle_img = np.zeros((height,width), np.uint8)
    return board,copy

if "__main__" == __name__:
    image = cv2.imread("/Users/martintin/Downloads/IMG_0866 2.JPG")
    cv2.imshow("frame",setgrid(image))
    cv2.waitKey(0)

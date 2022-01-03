
from PIL import Image
import cv2
import imutils
print(cv2.__version__)
import numpy as np
import matplotlib.pyplot as plt
import math
image = cv2.imread('/Users/martintin/Desktop/Screen Shot 2021-12-31 at 11.02.42 PM.png')

#image = cv2.imread('/Users/martintin/Desktop/Google Downloads/550px-nowatermark-Win-at-Connect-4-Step-9-Version-2.jpeg')
#image = cv2.imread('/Users/martintin/Desktop/Screen Shot 2021-12-31 at 11.02.42 PM.png')


new_width = 500 # Resize
img_h,img_w,_ = image.shape
scale = new_width / img_w
img_w = int(img_w * scale)
img_h = int(img_h * scale)
image = cv2.resize(image, (img_w,img_h), interpolation = cv2.INTER_AREA)
copy = image.copy()

image = cv2.bilateralFilter(image,15,190,190) 


image = cv2.fastNlMeansDenoising(image,10,7,21)




edges = cv2.Canny(image, 60,120)

cv2.imshow("output", edges)
cv2.waitKey(0)

uImg = image.copy()


contours, hierarchy = cv2.findContours(edges
, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
font = cv2.FONT_HERSHEY_COMPLEX

rects = []

good_contours = []
for contour in contours:
    cnt = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True) 
    x,y,w,h = cv2.boundingRect(cnt)
    area = w*h
    d=w
    c = math.pi*d
    if(len(cnt) >= 8 and 100*(w/h) > 80 and 100*(h/w) > 80 and c >= cv2.arcLength(cnt,True)-15 and c <= cv2.arcLength(cnt,True)+15         ):    
        rects.append([x,y,w,h])
        good_contours.append(cnt)
     
    
    

avg_area = int(math.trunc(sum([r[2]*r[3] for r in rects])/len(rects)))


for rect in rects:
    a = rect[2]*rect[3]
    if not(a in range(avg_area-5,avg_area+5)):
        index = rects.index(rect)
        del rects[index]
        del good_contours[index]

for rect,cnt in zip(rects,good_contours):
    x,y,w,h = rect
    #cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
    #cv2.drawContours(image, [cnt], 0, (0), 1)

cv2.imshow("jhi",image)
cv2.waitKey(0) 
avg_width = sum([r[2] for r in rects])/len(rects)
avg_height = sum([r[3] for r in rects])/len(rects)

#make grid
rows, cols = 7,6

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

spacing_x = width/(rows-1)
spacing_y = height/(cols-1)

radius = int((avg_width+avg_height)/4)






height,width,depth = copy.shape

circle_img = np.zeros((height,width), np.uint8)

hsv = cv2.cvtColor(copy, cv2.COLOR_BGR2HSV)
cv2.imshow("",hsv)
cv2.waitKey(0)

for row in range(rows):
    for col in range(cols):
        
        x = int(min_x+spacing_x*(row)+radius)
        y = int(min_y+spacing_y*(col)+radius)
        
        cv2.circle(circle_img,(x,y),radius+5,1,-1)

        red_lower = np.array([0, 50, 20])
        red_upper = np.array([5, 255, 255])
        
        
        
        
        mask = cv2.inRange(hsv, red_lower, red_upper)
        mask = cv2.bitwise_and(mask,circle_img)
        thingy = cv2.bitwise_and(hsv,hsv,mask=mask)

        num_red = cv2.countNonZero(mask)
        percent_red = (num_red/(math.pi*radius*2))*100
        #print((math.pi*math.pow(radius,2)),num_red)
        #cv2.imshow("hi",thingy)
        #cv2.waitKey(0)
        
        if(percent_red > 20):
            cv2.circle(image,(x,y),radius,(0,0,255),-1)
        else:

                yellow_lower = np.array([20, 100, 100])
                yellow_upper = np.array([30, 255, 255])


                circle_img = np.zeros((height,width), np.uint8)
                cv2.circle(circle_img,(x,y),radius,1,-1)
                mask1 = cv2.inRange(hsv, yellow_lower, yellow_upper)
                mask1 = cv2.bitwise_and(mask1,circle_img)
                thingy1 = cv2.bitwise_and(hsv,hsv,mask=mask1)

                num_yellow = cv2.countNonZero(mask1)
                percent_yellow = (num_yellow/(math.pi*radius*2))*100

                #cv2.imshow("hi",thingy)
            # cv2.waitKey(0)
                
                if(percent_yellow > 20):
                    cv2.circle(image,(x,y),radius,(0,255,255),-1)
                else:
                    cv2.circle(image,(x,y),radius,(0,0,0),1)

                

        circle_img = np.zeros((height,width), np.uint8)


        

        
       

    #    if(dist(RED,mean) < 300 and dist(YELLOW,mean) > 170):
    #        cv2.circle(image,(x,y),radius,(0,0,255),-1)
     ##   elif(int(dist(RED,mean)) in range(140,230) and int(dist(YELLOW,mean)) in range(100,290)):
     #       cv2.circle(image,(x,y),radius,(0,255,255),-1)
     #   else:
      #      cv2.circle(image,(x,y),radius,(0,0,0),1)
       # circle_img = np.zeros((height,width), np.uint8)
        
cv2.imshow("hi",image)
cv2.waitKey(0)


      
        
        
   
#cv2.bitwise_and(copy,copy,mask=circle_img)

cv2.imshow("hi",image)
cv2.waitKey(0)
        
        
        
        

        
       





cv2.destroyAllWindows()

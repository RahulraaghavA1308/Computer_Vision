import cv2 as cv
import numpy as np

blank =np.zeros((500,500,3),dtype='uint8')
img =cv.imread('Cat.jpg')


#cv.imshow('Blank', blank)
#cv.imshow('cat', img)
#paint the image 
blank[200:300 ,300:400]=10,20,30
#cv.imshow('Blank', blank)
#drawing a rectangle
cv.rectangle(blank ,(0,0),(250,250),(0,250,50),thickness=3)
#cv.imshow('rectangle',blank)
cv.rectangle(blank ,(0,0),(250,250),(0,250,50),thickness=cv.FILLED)
#cv.imshow('rectangle2',blank)
cv.rectangle(blank ,(0,0),(blank.shape[1]//2,blank.shape[2]//2),(0,250,50),thickness=cv.FILLED)
#cv.imshow('rectangle2',blank)

#draw a circle
cv.circle(blank,(250,250),50,(0,50,50),thickness=10)
#cv.imshow('circle',blank)
#draw a line
cv.line(blank,(20,20),(120,120),(0,0,200),thickness=5)
#cv.imshow('Line',blank)
#write text 
cv.putText(blank,'Hello i am rahul',(0,365),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,200,200),thickness=2)
cv.imshow('text',blank)

cv.waitKey(0)


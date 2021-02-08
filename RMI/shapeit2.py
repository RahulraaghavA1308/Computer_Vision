import cv2 as cv
import numpy as np
font = cv.FONT_HERSHEY_COMPLEX

img =cv.imread('shapes.jpg')
cv.imshow('original',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

ret, thresh =cv.threshold(gray,230,255,cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)

contours,hierarchies =cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)

blank2 =np.zeros(img.shape,dtype ='uint8')
blank =np.zeros(img.shape,dtype ='uint8')
cv.drawContours(blank,contours,-1,(255,0,0),thickness=2)
cv.imshow('drawn contours',blank)

for cnt in contours:
    epsilon = 0.02*cv.arcLength(cnt,True)
    approx =cv.approxPolyDP(cnt,epsilon,True)
    # print(len(approx))
    cv.drawContours(blank2,[approx],-1,(0,0,255),thickness=2)
    x=approx.ravel()[0]
    y=approx.ravel()[1]
    print(x,y)
    if len(approx) == 4:
        cv.putText(blank2, "Rectangle", (x, y), font,1 , (0,255,0))
  
cv.imshow('approx',blank2)
cv.waitKey(0)
cv.destroyAllWindows
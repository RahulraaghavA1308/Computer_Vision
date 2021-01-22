import cv2 as cv
import numpy as np

img =cv.imread('Cat.jpg')
cv.imshow('norm', img)

blank = np.zeros(img.shape,dtype ='uint8')

# Finding no of contours
blur=cv.GaussianBlur(img,(1,1),cv.BORDER_DEFAULT)
gray= cv.cvtColor(blur,cv.COLOR_BGR2GRAY)
canny =cv.Canny(gray,125,175)
#cv.imshow('canny', canny)
#threshold
ret, thresh = cv.threshold(gray,125,255, cv.THRESH_BINARY)
#cv.imshow('Thresh', thresh)

contours ,hierarchies =cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)}  is the no of contours')

contours1 ,hierarchies =cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours1)}  is the no of contours')

cv.drawContours(blank,contours,-1,(0,0,200),thickness=1)
cv.imshow('Contourdrawn',blank )

#cv.waitkey(0)
while True:    
    if cv.waitKey(20) &0xFF==ord('d'):
            break;
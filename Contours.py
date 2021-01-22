import cv2 as cv
import numpy as np
# Finding no of contours
img =cv.imread('Cat.jpg')
blur=cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
gray= cv.cvtColor(blur,cv.COLOR_BGR2GRAY)
canny =cv.Canny(gray,125,175)
cv.imshow('canny', canny)

contours ,hierarchies =cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)}  is the no of contours')

#cv.waitkey(0)}

while True:    
    if cv.waitKey(20) &0xFF==ord('d'):
            break;
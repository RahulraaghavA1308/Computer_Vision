import cv2 as cv
import numpy as np

img =cv.imread('Cat.jpg')
cv.imshow('cat1', img)
#gray scale convertion
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('cat', gray)

#blur
blur=cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)

#EDGE cascade
canny =cv.Canny(blur,125,175)
cv.imshow('canny', canny)

#Dilating the image 
dilated = cv.dilate(canny,(3,3),iterations=5)
#cv.imshow('dilated', dilated)

#eroding
erode=cv.erode(dilated,(3,3),iterations=5)
#cv.imshow('eroded', erode)

#resize
resize =cv.resize(img,(500,500))
cv.imshow('resize', resize)

#cropping
cropped =img[0:200,100:400]
cv.imshow('Crop', cropped)

#cv.waitkey(0)
while True:    
    if cv.waitKey(20) &0xFF==ord('d'):
            break;
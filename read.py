import cv2 as cv
import numpy as np
img =cv.imread('Cat.jpg')
blank =np.zeros((500,500),dtype='uint8')
cv.imshow('Blank', blank)

cv.imshow('cat', img)

#cv.imshow('Cat', img)
capture = cv.VideoCapture('Solar.mp4')
while True:
    isTrue, frame =capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) &0xFF==ord('d'):
        break;

capture.release()
cv.destroyAllWindows()

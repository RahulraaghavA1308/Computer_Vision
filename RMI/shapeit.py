import cv2 as cv
import numpy as np

img = cv.imread("shapes.jpg", cv.IMREAD_GRAYSCALE)
#cv.imshow("gray",img)
blank = np.zeros(img.shape,dtype ='uint8')

# blur=cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
# cv.imshow("blur",blur)
ret, thresh = cv.threshold(img,240,255, cv.THRESH_BINARY)
#cv.imshow("Thresh",thresh)

canny =cv.Canny(img,125,175)
#cv.imshow('canny', canny)
contours ,hierarchies =cv.findContours(canny,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
cnt =contours[11]
cv.drawContours(img,[cnt],0,(0,0,200),thickness=3)
cv.imshow('Contour drawn',img)


# for cnt in contours:
#     approx = cv.approxPolyDP(cnt, 0.05*cv.arcLength(cnt, True), True)
#     cv.drawContours(img, [approx], 0, (0), 5)

cv.imshow('Contour drawn',img)

cv.waitKey(0)
cv.destroyAllWindows
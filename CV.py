import cv2 as cv


img =cv.imread('Cat.jpg')

def changeres(width,height):#live videos  Don't use this genearaly
    capture.set(3,width)
    capture.set(4,height)

def rescaleframe(frame, scale=0.75):#for images ,videos,live videos
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[1]*scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


resized_image= rescaleframe(img)
cv.imshow('Cat' , resized_image)


capture = cv.VideoCapture('Solar.mp4')
while True:
    isTrue, frame =capture.read()
    frame_resized  = rescaleframe(frame)
    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)
    
    if cv.waitKey(20) &0xFF==ord('d'):
        break;

capture.release()
cv.destroyAllWindows()
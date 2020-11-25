import cv2 as cv
import numpy as np

cam=cv.VideoCapture(0)

codec =cv.VideoWriter_fourcc(*'XVID')

output = cv.VideoWriter('capture.avi',codec,20.0,(640,480))

lowerb = np.array([150,0,200])
upperb = np.array([255,150,255])


while(1):
    ret, frame = cam.read()
    frame = cv.GaussianBlur(frame,(5,5),0)

    edges = cv.Canny(frame,100,200)

    img = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    cv.imshow('video',frame)

##    cv.imshow('video1',img1)

   
    img1 = cv.inRange(img,lowerb,upperb)
##    cv.imshow('ball',img1)

    cv.imshow('edge',edges)
    
    key = cv.waitKey(20) & 0xFF
    if key==27:
        break
    
cam.release()


cv.destroyAllWindows()

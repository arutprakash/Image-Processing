import cv2 as cv
import numpy as np

cam = cv.VideoCapture(0)

lowerb = np.array([150,0,200])
upperb = np.array([255,150,255])



while(1):
    ret,frame = cam.read()
    frame = cv.GaussianBlur(frame,(5,5),0)
    cv.imshow('video',frame)

    hsv= cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    ball = cv.inRange(hsv, lowerb, upperb)

    img2,contours,h = cv.findContours(ball,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)

##    con = cv.drawContours(frame,contours,-1,(255,0,0),4)
##
##    cv.imshow('con',frame)

    cnt=np.array([])
    if len(contours)>0:
        cnt=contours[0]
        (x,y),radius = cv.minEnclosingCircle(cnt)
        center = (int(x),int(y))
        radius = int(radius)
        cv.circle(frame,center,radius,(0,255,0),2)
      

    cv.imshow('con',frame) 
    key = cv.waitKey(20) & 0xFF
    if key==27:
        break
    
cam.release()


cv.destroyAllWindows()
 

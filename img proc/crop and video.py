import cv2 as cv
import numpy as np
img = cv.imread('messi5.jpg', -1)
cv.imshow('messi',img)

###img1 = cv.imread('messi5.jpg', 0)
##cv.imshow('messi1',img1)


##img[100:150,200:250] = [255,255,255]
##img[100:150,200:250,1] = 5
##cv.imshow('messi1',img)

##hsv=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
##cv.imshow('hsv', hsv)

##
##h,s,v = cv.split(img)
##cv.imshow('h',h)
##cv.imshow('s',s)
##cv.imshow('v',v)


cam=cv.VideoCapture(0)

while(1):
    ret, frame = cam.read()
    cv.imshow('video',frame)
    cv.waitKey(1)
    if cv.waitKey(200) & 0xFF == ord('q'):
        break
    
cam.release()
cv.waitKey(0)

cv.destroyAllWindows()

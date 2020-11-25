import cv2
import numpy

image = cv2.imread('p.jpg')

cv2.imshow('image',image)

b,g,r = cv2.split(image)

cv2.imshow('b',b)
cv2.imshow('g',g)
cv2.imshow('r',r)
k= cv2.waitKey(0)

if k==27:
    cv2.destroyALLWindows()
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('sudoku.png',0)
img = cv.GaussianBlur  (img,(5,5),0)

ret1, threshold1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
##ret2, threshold2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)

threshold2= cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
threshold3= cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)

##ret2, threshold3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
##ret2, threshold4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
##ret2, threshold5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)

##cv.imshow('actual',img)
##cv.imshow('threshold1',threshold1)
##cv.imshow('threshold2',threshold2)
##cv.imshow('threshold3',threshold2)
##cv.imshow('threshold4',threshold2)
##cv.imshow('threshold5',threshold2)


images = [img, threshold1, threshold2, threshold3]##, threshold4, threshold5]
titles= ['actual','binary','adaptive_mean','adaptive_gauss']##'binary_inv','trunc','t0zero','tozero_inv']

plt.subplot(2,3,1)

for i in xrange(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()


cv.waitKey(0)

cv.destroyAllWindows()






                               

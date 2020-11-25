import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('noisy2.png')

##blur = cv.blur(img,(9,9))
##blur =cv.GaussianBlur(img,(9,9),0)
##blur = cv.bilateralFilter(img,9,75,75)
blur = cv.medianBlur(img,9)

plt.subplot(1,2,1),plt.imshow(img),plt.title('orginal')
plt.xticks([]),plt.yticks([])
plt.subplot(1,2,2),plt.imshow(blur),plt.title('blur')
plt.xticks([]),plt.yticks([])


plt.show()

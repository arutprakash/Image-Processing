import cv2 as cv
import numpy as np

bgr = np.array([[[197,22,250]]],dtype=np.uint8)

hsv = cv.cvtColor(bgr, cv.COLOR_BGR2HSV)

print(hsv)


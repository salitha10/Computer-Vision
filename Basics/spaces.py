import cv2 as cv
import numpy as np

img = cv.imread('../media/cat1.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# RBG to HSV
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)



cv.waitKey(0)
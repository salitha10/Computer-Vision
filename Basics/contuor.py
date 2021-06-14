import cv2 as cv
import numpy as np

img = cv.imread('../media/cat1.jpg')

#Blank canvas
blank = np.zeros(img.shape, dtype='uint8')

canny = cv.Canny(img, 125,175)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)

#Threshold
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)

cv.imshow('Cat', thresh)

#Find contuors
coutuors, hirrachy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
print(len(coutuors))

cv.drawContours(blank, coutuors, -1, (0,0,255), 2)
cv.imshow('Contours', blank)

cv.waitKey(0)
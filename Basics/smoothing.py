import cv2 as cv
import numpy as np

img = cv.imread('../media/cat1.jpg')
cv.imshow('Cat', img)

#Averaging
average = cv.blur(img, (3,3))
cv.imshow('Blur', average)

#Agusian blur
gausian = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gausian Blur', gausian)

#Median blur
median = cv.medianBlur(img, 3)
cv.imshow('Median', median)

#Bilateral (Most effective)
bilateral = cv.bilateralFilter(img, 5, 25, 30)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)
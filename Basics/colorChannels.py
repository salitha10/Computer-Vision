import cv2 as cv
import numpy as np

img = cv.imread('../media/cat1.jpg')

#Split colors
b, g, r = cv.split(img)

blank = np.zeros(img.shape[:2], dtype='uint8')

#Seperate colors
blue = cv.merge([b,blank, blank])
green = cv.merge([blank,g, blank])
red = cv.merge([blank,blank, r])

cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)

print(b.shape)
print(g.shape)
print(r.shape)

#Merge channels
merged = cv.merge([b,g,r])
cv.imshow('Merged', merged)

cv.waitKey(0)
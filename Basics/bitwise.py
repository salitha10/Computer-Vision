import cv2 as cv
import numpy as np


blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow("Circe", circle)

#Bitwise AND
bitwiseAND = cv.bitwise_and(rectangle, circle)
cv.imshow("AND", bitwiseAND)

#Birtwise OR
bitwiseOR = cv.bitwise_or(rectangle, circle)
cv.imshow("OR", bitwiseOR)

#Bitwise XOR -> Non Intersecting regions
bitwiseXOR = cv.bitwise_xor(rectangle, circle)
cv.imshow('XOR', bitwiseXOR)

#Bitwise NOT -> Invert colors
bitwiseNOT = cv.bitwise_not(rectangle)
cv.imshow('NOT', bitwiseNOT)

# img = cv.imread('../media/cat1.jpg')
# cv.imshow('Cat', img)

cv.waitKey(0)
import cv2 as cv
import numpy as np

img = cv.imread('../media/cat1.jpg')

blank = np.zeros(img.shape[:2], dtype='uint8')

#Mask
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2 + 45), 100, 255, -1)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("Masked", masked)

cv.waitKey(0)
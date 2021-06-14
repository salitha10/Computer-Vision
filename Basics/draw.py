import cv2 as cv
import numpy as np

#Blank canvas
blank = np.zeros((500,500,3), dtype='uint8')

#blank[200:300, 300:400] = 0,255,0

#Draw rectangle
cv.rectangle(blank, (0,0), (blank.shape[0]//2, blank.shape[1]//2), (0,250,0), thickness=2)

#Draw circle
cv.circle(blank, (blank.shape[0]//2, blank.shape[1]//2), 40, (250,0,0), thickness=-1)

#Line
cv.line(blank, (100,350), (blank.shape[0]//2, blank.shape[1]//2), (255,2555,0), thickness=2)

#Text
cv.putText(blank, "Hello", (255,255), cv.FONT_ITALIC, 1.0, (0,255,0), thickness=2)

cv.imshow('Blank', blank)
cv.waitKey(0)
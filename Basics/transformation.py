import cv2 as cv
import numpy as np

img = cv.imread("../media/cat1.jpg")

#Translate
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


translated = translate(img, 100, 100)

#Rotate
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

#rotate
rot = rotate(img, 45)

#Resize
recized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)

#Flip
flip = cv.flip(img, 0)
cv.imshow('Cat', flip)

cv.waitKey(0)
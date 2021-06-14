import cv2 as cv

img = cv.imread('../media/cat1.jpg')

#Convert to gray image
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#Blur
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)

#Edge cascade
canny = cv.Canny(blur, 125, 175)

#Dilate image
dilate = cv.dilate(canny, (3, 3), iterations=3)

#Eroding
eroded = cv.erode(dilate, (3, 3), iterations=3)

#Resize
resize = cv.resize(img, (500,500), interpolation=cv.INTER_LINEAR)

#Crop
cropped = img[50:500, 200:400]
cv.imshow('Cat', cropped)


cv.waitKey(0)
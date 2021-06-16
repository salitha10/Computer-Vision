import cv2 as cv
import cv2.data

img = cv.imread('../media/group1.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#Haaar cascade
haar_cascade = cv.CascadeClassifier('haar_face.xml')

#Detectv -> list of coordinates
face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5) #Change minNeighbour to get more accurate results

print(f'Number of faces found = {len(face_rect)}')

#Print face rectangle
for (x,y,w,h) in face_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

resize = cv.resize(gray, (600,500), interpolation=cv.INTER_LINEAR)
cv.imshow('Girl', img)

cv.waitKey(0)

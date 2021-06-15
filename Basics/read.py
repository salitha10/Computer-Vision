import cv2 as cv

#Read image
# img = cv.imread('../media/cat1.jpg')

#Display image
# cv.imshow('Cat', img)

#Rescale
def rescaleFrame(frame, scale=0.25 ):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

#Change resolution for live videos
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4,height)

# cv.waitKey(0)


#Read video
capture = cv.VideoCapture('media/Dog1.mp4')

#Reaad frame by frame
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break;

#Release resources
capture.release()
cv.destroyWindow('Video')




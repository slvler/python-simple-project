import cv2 as cv
import numpy as np

camera = cv.VideoCapture(0)

while True:
    _, frame = camera.read()
    cv.imshow('Camera', frame)

    laplacian = cv.Laplacian(frame, cv.CV_64F)
    laplacian = np.uint8(laplacian)
    cv.imshow('laplacian', laplacian)


    edges = cv.Canny(frame, 120, 120)
    cv.imshow('Canny', edges)

    if cv.waitKey(5) == ord('x'):
        break



camera.release()
cv.destroyAllWindows()
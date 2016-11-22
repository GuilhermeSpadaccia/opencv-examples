import cv2
import sys
import datetime, time, math
from math import sqrt
import numpy

video_capture = cv2.VideoCapture(0)
firstFrame = None;

while True:
    #faz a aquisicao do frame
    ret, frame = video_capture.read()
    frame = cv2.flip(frame,0)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray2 = cv2.Laplacian(gray,cv2.CV_64F)
    laplace = cv2.convertScaleAbs(gray2)

    laplace = cv2.blur(laplace, (5, 5), 0)
    
    if firstFrame is None:
        firstFrame = laplace
        continue
    
    cv2.imshow('Video1', frame)
    cv2.imshow('Video2', laplace)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

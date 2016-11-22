import cv2
import sys

image = cv2.VideoCapture(0)
      
while True:

    ret, frame = image.read()
    frame = cv2.flip(frame,0)

    cv2.imshow('WebCam', frame)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
image.release()
cv2.destroyAllWindows()

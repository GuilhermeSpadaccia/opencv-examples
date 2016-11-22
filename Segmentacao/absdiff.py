import cv2
import sys

image1 = cv2.VideoCapture(0)
image2 = cv2.VideoCapture(0)
count = None
      
while True:

    if count == 5 or count == None:
        ret1, frame1 = image1.read()
        frame1 = cv2.flip(frame1,0)
        gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        count = 0
    else:
        count+=1

    ret2, frame2 = image2.read()
    frame2 = cv2.flip(frame2,0)
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    
    a = cv2.absdiff(gray,gray2)

    tst = cv2.addWeighted(a, 1.5, gray2, -2, 1)
    
    cv2.imshow('absdiff', a)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
image1.release()
image2.release()
cv2.destroyAllWindows()

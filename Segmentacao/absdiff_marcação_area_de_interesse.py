import cv2
import sys
import numpy as np

image1 = cv2.VideoCapture(0)
image2 = cv2.VideoCapture(0)
count = None
      
while True:

    ret1, frame1 = image1.read()
    frame1 = cv2.flip(frame1,0)
    gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

    ret2, frame2 = image2.read()
    frame2 = cv2.flip(frame2,0)
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    
    MedianBlur = cv2.medianBlur(gray, 11)
    MedianBlur = cv2.medianBlur(gray2, 11)
    
    absdiff = cv2.absdiff(gray,gray2)

    thresh = cv2.threshold(absdiff, 25, 255, cv2.THRESH_BINARY)[1]

    #kernel = np.ones((5,5),np.uint8)
    dilation = cv2.dilate(thresh,None,iterations = 8)
    erosion = cv2.erode(dilation,None,iterations = 5)

    #edges = cv2.Canny(erosion,50,100)
    (contours, a, _) = cv2.findContours(erosion.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    minarea = 1000
    for i in range(0, len(a)):
        if cv2.contourArea(a[i]) > minarea:
            maxsize = cv2.contourArea(a[i])
            x,y,w,h = cv2.boundingRect(a[i])

            cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow('absdiff', absdiff)
    cv2.imshow('Detection', frame1)
    
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
image1.release()
image2.release()
cv2.destroyAllWindows()

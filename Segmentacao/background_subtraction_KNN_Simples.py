'''
    http://docs.opencv.org/master/db/d5c/tutorial_py_bg_subtraction.html#gsc.tab=0
'''
import numpy as np
import cv2

#funcao para o sort
def getKey(item):
        return item[0]

cap = cv2.VideoCapture(0)

#Duas formas de se fazer o Background Subtraction
#fgbg = cv2.createBackgroundSubtractorMOG2()
fgbg = cv2.createBackgroundSubtractorKNN()
fgbg.setHistory(100000)

count = 0
while(True):
        ret, frame = cap.read()
        frame = cv2.flip(frame,0)
        #Como minha webcam eh ruim, espero os 20 primeiros frames para o obturador se adaptar
        if count == 20:

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                
                MedianBlur = cv2.medianBlur(gray, 11)
                        
                #aplica o BG Subtraction
                fgmask = fgbg.apply(MedianBlur)

                #exibo as imagens
                cv2.imshow('mark', fgmask)
                cv2.imshow('frame', frame)

                k = cv2.waitKey(30) & 0xff
                if k == 27:
                        break
        else:
                count += 1

cap.release()
cv2.destroyAllWindows()
        

import cv2
import numpy as np

image = cv2.VideoCapture(0)
      
while True:

    ret, frame = image.read()
    frame = cv2.flip(frame,0)

    #Gera uma mascara com ancoragem no pixel central
    kernel = np.ones((5,5),np.uint8)

    #Dilatacao - Aplica a mascara na imagem alterando o pixel central
    #com o pixel maximo
    dilation = cv2.dilate(frame,kernel,iterations = 2)

    #Erosao - Aplica a mascara na imagem alterando o pixel central
    #com o pixel minimo
    erosion = cv2.erode(frame,kernel,iterations = 2)
    
    cv2.imshow('Erosion', erosion)
    cv2.imshow('Dilation', dilation)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
image.release()
cv2.destroyAllWindows()

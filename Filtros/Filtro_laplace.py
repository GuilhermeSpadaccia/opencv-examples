import cv2

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    frame = cv2.flip(frame,0)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #gauss = cv2.GaussianBlur(gray, (11, 11), 0)
    
    laplace = cv2.Laplacian(gray,cv2.CV_64F)

    cv2.imshow('Laplace', laplace)
    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()

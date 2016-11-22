import cv2
import sys

# Get user supplied values
image = cv2.VideoCapture(0)
cascPath = "haarcascade_frontalface_default.xml"

while True:
    
    ret, frame = image.read()
    newImage = cv2.flip(frame,0)
    
    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Convert to gray scale
    gray = cv2.cvtColor(newImage, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(10, 10),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    print "Found {0} faces!".format(len(faces))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(newImage, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    cv2.imshow("Faces found", newImage)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

image.release()
cv2.destroyAllWindows()

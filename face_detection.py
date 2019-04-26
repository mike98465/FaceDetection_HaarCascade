import cv2
import sys
import numpy as np
from PIL import Image

# Get user supplied values
cascPath = "haarcascade_frontalface_alt2.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread('test7.jpg')
#image = cv2.resize(image, (max(1000, image.shape[1]),max(1000, image.shape[0])), interpolation=cv2.INTER_LINEAR )
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.05,
    minNeighbors=5,
    minSize=(30, 30)
    #flags = cv2.CV_HAAR_SCALE_IMAGE
)

print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 4)

while(1):
	cv2.imshow("face detection", image)
	
	#press "enter" to exit
	if cv2.waitKey(1) == 13:
		break
	
cv2.destroyAllWindows()
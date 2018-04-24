#detects face real time

import numpy as np
import cv2
import time
from facedetection import is_image_with_face


cap = cv2.VideoCapture(0)

haar_face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
start_time = time.time()

while (True):
	
	#Capture frame-by-frame
	ret, frame = cap.read()

	if (is_image_with_face(haar_face_cascade, frame)):
		print("face detected")
	else:
		print("no face")

	cv2.imshow('frame', frame)

	if (cv2.waitKey(1) & 0xFF == ord('q')):
		break

cap.release()
cv2.destroyAllWindows()
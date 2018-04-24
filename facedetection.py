#!/usr/bin/env python

import cv2

# Returns if a face was detected in a certain image
def is_image_with_face(f_cascade, colored_img, scaleFactor = 1.1):
	# Copies input image
	img_copy = colored_img.copy()

	# Converts copied image to grayscale
	gray_img = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)

	# Detects multiscale images
	faces = f_cascade.detectMultiScale(gray_img, scaleFactor = scaleFactor, minNeighbors = 5)
	
	for (x, y, w, h) in faces:
		cv2.rectangle(img_copy, (x,y), (x+w, y+h), (0,255,0), 2)
    # Returns true if at least one face was detected, otherwise returns false
	return len(faces) > 0


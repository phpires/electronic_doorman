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

    # Returns true if at least one face was detected, otherwise returns false
    return len(faces) > 0

# Loads the classifiers
haar_face_cascade = cv2.CascadeClassifier('opencv/data/haarcascades/haarcascade_frontalface_default.xml')
lbp_face_cascade = cv2.CascadeClassifier('opencv/data/lbpcascades/lbpcascade_frontalface.xml')

# Asks for the name of the image file
img_name = raw_input('Enter the name of the image file (including its extension): ')

# Loads the image
img = cv2.imread(img_name)

# Runs the face detection function
print is_image_with_face(haar_face_cascade, img)
print is_image_with_face(lbp_face_cascade, img)


import cv2
from random import randrange

# Lode some pre-trained data on face frontals from opencv
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Choose an image to detect face in
# img = cv2.imread('RDJ.png')
# img = cv2.imread('taylor.png')
# img = cv2.imread('set2.png')

# To capture to grayscale
webcam = cv2.VideoCapture(0) # can mp4

# Insert forever over frames
while True:

    # Read the current frame
    successful_frame_reade, frame = webcam.read()

    # must convert to grayscale
    grayscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect Faces
    face_coordinates = trained_face_data.detectMultiScale(grayscale_img)

    # Draw rectangle
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 8)

    cv2.imshow('Face Detector' , frame)
    key = cv2.waitKey(1)

    # Stop if 0 key is pressed
    if key==81 or key==113:
        break

# release the webcam
webcam.release()

print("Code Complete")
"""
# Detect Faces
face_coordinates = trained_face_data.detectMultiScale(grayscale_img)

# Draw rectangle
for (x, y, w, h) in face_coordinates:
#  (x, y, w, h) = face_coordinates[0] --> 1 face
    cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 8)


# (x, y, w, h) = face_coordinates[1]
# cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 8)
# cv2.rectangle(img, (145, 57), (145+161, 57+161), (0, 255, 0), 2)

# print(face_coordinates)

# Display image with the faces
cv2.imshow('Face Detector' ,img)
cv2.waitKey()

print("Code Complete")
"""
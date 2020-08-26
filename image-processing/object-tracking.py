import cv2
import numpy as np

# Video Capturing
cap = cv2.VideoCapture(0)

while True:
    # Read frame
    _, frame = cap.read()

    # Convert from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # set upper and lower limits to detect blue color
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([110, 255, 255])

    # defining blue mask
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # applying mask
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    key = cv2.waitKey(5) & 0xFF
    if key==ord('q'):
        break

cv2.destroyAllWindows()

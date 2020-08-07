import numpy as np
import cv2

cap = cv2.VideoCapture(-1)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capture frame by frame
    ret, frame = cap.read()

    if not ret:
        print("Couldn't read from video source")
        break
    
    # image operations goes here
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('webcam', frame)
    if cv2.waitKey(1)==ord('q'):
        print("Closing program...")
        break
cap.release()
cv2.destroyAllWindows()

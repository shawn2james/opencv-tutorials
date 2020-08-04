import numpy as np
import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('../files/saved-video.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Couldn't read from video source! Exiting...")
        break
    frame = cv2.flip(frame, 0)

    # writing to file
    out.write(frame)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()

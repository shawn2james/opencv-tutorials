import numpy as np
import cv2

cap = cv2.VideoCapture('../files/demo.gif')

while cap.isOpened():
    ret, frame = cap.read()
    # print current position of the video file in milliseconds
    print(cap.get(cv2.CAP_PROP_POS_MSEC))
    # if frame is read correctly, ret = True
    if not ret:
        print("Can't recieve frame from video source! Exiting...")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('demo.gif', gray)
    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

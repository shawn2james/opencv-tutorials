import numpy as np
import cv2

# print all the events available in opencv
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

# mouse callback function
def draw_circle(event, x, y, flags, param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1)

# create a blank image and bind mouse event to draw_circle function
img = np.zeros((512, 512, 3), dtype=np.uint8 )
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()

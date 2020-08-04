import numpy as np
import cv2

img = cv2.imread('../files/sun.jpg')

# drawing a line on image
cv2.line(img, (0, 0), (230, 200), (0, 0, 255), 5)
# drawing a rectangle on image
cv2.rectangle(img, (300, 100), (500, 300), (255, 255, 255), 2)
# drawing a circle on image
cv2.circle(img, (400, 200), 50, (255, 0, 0), -1)
# drawing an ellipse
cv2.ellipse(img, (256, 400), (100, 50), 0, 0, 180, 255, -1)
# drawing a polygon
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 70]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (0, 255, 255))
# adding text to image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV Tutorials', (10, 450), font, 4, (255, 255, 255), 4, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

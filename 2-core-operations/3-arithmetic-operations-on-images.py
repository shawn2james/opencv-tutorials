import numpy as np
import cv2

img1 = cv2.imread('../files/sun.jpg')
img2 = cv2.imread('../files/mountain.jpg')
img1 = cv2.resize(img1, (500, 400), cv2.INTER_AREA)
img2 = cv2.resize(img2, (500, 400), cv2.INTER_AREA)

# Image Addition
added = cv2.add(img1, img2)

# Image Blending
blended = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

cv2.imshow('Added', added)
cv2.imshow('Blended', blended)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2 
import numpy as np
import os

img = cv2.imread('../files/mountain.jpg')

# Scaling
scaled = cv2.resize(img, dsize=None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# Translation
height, width, _ = img.shape
                    # x-shift    # y-shift
M = np.float32([[1, 0, 100], [0, 1, 50]])
translated = cv2.warpAffine(img, M, (width, height))

# Rotation
M = cv2.getRotationMatrix2D( ( (width-1)/2, (height-1)/2 ), 90, 1)
rotated = cv2.warpAffine(img, M, (width, height))

cv2.imshow('Scaled Image', scaled)
cv2.imshow('Translated Image', translated)
cv2.imshow('Rotated Image', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
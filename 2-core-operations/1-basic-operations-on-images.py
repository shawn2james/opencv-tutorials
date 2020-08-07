import numpy as np
import cv2

img = cv2.imread('../files/messi.jpg')

# ACCESSING AND MODIFYING PIXEL VALUES
# 1 => directly accesing via indexing
img[100:150, 100:150] = [255, 255, 255]
# 2 => better editing method
img.itemset((150, 150, 0), 255) # => sets the Blue value at (150, 150) to 255

# ACCESSING IMAGE PROPERTIES
print(img.shape)
print(img.size)
print(img.dtype)

# REGION OF INTEREST (ROI)
# duplicating the ball in the image 
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

# SPLITTING AND MERGING IMAGE CHANNELS
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

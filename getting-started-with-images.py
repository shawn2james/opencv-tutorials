import cv2
import sys

img = cv2.imread('images/mountain.jpg')

if img is None:
    sys.exit("Could not read the image")

cv2.imshow("Image", img)
key = cv2.waitKey(0)

if key==ord('s'):
    cv2.imwrite("images/mountain-saved.jpg", img)

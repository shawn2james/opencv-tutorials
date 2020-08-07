import numpy as np
import cv2
import matplotlib.pyplot as plt

BLUE = [255, 0, 0]

img = cv2.imread('../files/messi.jpg')

replicate = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=BLUE)

plt.subplot(231)
plt.imshow(img, 'gray')
plt.title('ORIGINAL')

plt.subplot(232)
plt.imshow(replicate, 'gray')
plt.title('REPLICATE')

plt.subplot(233)
plt.imshow(reflect, 'gray')
plt.title('REFLECT')

plt.subplot(234)
plt.imshow(reflect101, 'gray')
plt.title('REFLECT_101')

plt.subplot(235)
plt.imshow(wrap, 'gray')
plt.title('WRAP')

plt.subplot(236)
plt.imshow(constant, 'gray')
plt.title('CONSTANT')

plt.show()

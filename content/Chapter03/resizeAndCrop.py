import cv2
import numpy as np

img = cv2.imread('../Resources/lambo.png')
print('Height, width, RGB channels', img.shape)

imgResize = cv2.resize(img, (1000, 50))
print('Height, width, RGB channels', imgResize.shape)

imgCropped = img[0:200,200:500] # from 0 (top left) to 200 in Height, from 200 to 500 in Width
print('Height, width, RGB channels', imgCropped.shape)

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)

cv2.waitKey(0)
import cv2
#  load an image using 'IMREAD'
img = cv2.imread('../Resources/lena.png')
# display
cv2.imshow('Lena Soderberg', img)

# cv2.waitKey(0)

cv2.waitKey(5000) # 5 seconds



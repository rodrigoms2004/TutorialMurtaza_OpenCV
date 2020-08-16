import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
# print(img)
img[:] = 67,70,75 # background color Steel Grey https://www.htmlcsscolor.com/hex/43464B
print(img.shape)

# RGB (Red, Green, Blue)
# (0, 0, 0) = Black
# (255, 255, 255) = White
# (255, 0, 0) = Blue
# (0, 255, 0) = Green
# (0, 0, 255) = Red

# (255, 255, 0) = Blue + Green = Cyan
# (255, 0, 255) = Blue + Red = Magenta
# (0, 255, 255) = Green + Red = Yellow

# draws a line from point (0,0) top left to the point (512,512) bottom right
# with color green and thickness 3
cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (0, 255, 0), 3) 
# draws a red rectangle of height of 350 (y=350) and a width of 250 (x=250), thickness 2
cv2.rectangle(img, (0,0), (250, 350), (0,0,255), 2) # cv2.FILLED)
# draws a cyan circle of radius 30 in point (x=400, y=500), thickness 5
cv2.circle(img, (400, 500), 30, (255, 255, 0), 5)
# drans " OPENCV " in point (x=300, y=200) using font hershey complex, font scale 1, dark green, thickness 3 
cv2.putText(img, " OPENCV ", (300, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 3)


cv2.imshow('Image', img)
cv2.waitKey(3000) # 3 seconds

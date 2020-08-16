import cv2 as cv
import os

videoFile = os.stat('../Resources/test_video.mp4')
print(videoFile, '\n')

frameWidth = 640
frameHeight = 480

cap = cv.VideoCapture("../Resources/test_video2.mp4")
while True:
  success, img = cap.read()
  # img = cv.resize(img, (frameWidth,frameHeight))
  cv.imshow("Result", img)
  
  if cv.waitKey(1) and 0xFF == ord('q'):
    break

# Solved!
# pip install opencv-contrib-python

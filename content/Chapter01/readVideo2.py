import os
import cv2
import numpy as np

# https://www.programmersought.com/article/50002495152/

# listing = os.listdir('../Resources')
# print(listing[4])

vid = '../Resources/test_video.mp4'
frames = []
cap = cv2.VideoCapture(vid)

# Get some parameters of the video, here is the frame rate
fps = cap.get(5)
# print(fps)
# Obtain the total number of frames of video
x = cap.get(7)
print(x)

# for k in range(88):
while True:
  # Frame is the image of each frame, a three-dimensional matrix
  ret, frame = cap.read()
  # Resampling using pixel relationship. When the image is reduced when method avoids the occurence or ripples.
  try:
    frame = cv2.resize(frame, (320, 240), interpolation=cv2.INTER_AREA)
    print(frame.shape)
    cv2.imshow("Result", frame)
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # frames.append(gray)
  except EnvironmentError:
    break

  if cv2.waitKey(1) and 0xFF == ord('q'):
    break


# cap.release()
# cv2.destroyAllWindows()
# input = np.array(frames)
# print(input)
# ipt = np.rollaxis(np.rollaxis(input, 2, 0), 2, 0)


# frameWidth = 560
# frameHeight = 320

# cap = cv.VideoCapture("../Resources/test_video.mp4")
# while True:
#   success, img = cap.read()

  
#   img = cv.resize(img, (frameWidth,frameHeight), interpolation=cv.INTER_AREA)
#   cv.imshow("Result", img)
  
#   if cv.waitKey(1) and 0xFF == ord('q'):
#     break


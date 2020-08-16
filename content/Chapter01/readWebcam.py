import cv2
frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
# cap.set(10, 150) # brightness 
cap.set(cv2.CAP_PROP_BRIGHTNESS, 150) # brightness 

# Video properties
# https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d

while True:
  success, img = cap.read()
  cv2.imshow("Result", img)
  if cv2.waitKey(1) and 0xFF == ord('q'):
    break
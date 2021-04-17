import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(r"C:\Users\kunal\Videos\handTestVideo.mp4")

while True:
      success, img = cap.read()

      cv2.imshow("Hand", img)
      cv2.waitKey(1)




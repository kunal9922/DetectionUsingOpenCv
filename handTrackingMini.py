import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(r"dataSet\handTestVideo.mp4")
#import the class  from mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands()

while True:
      success, img = cap.read()
      imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
      results = hands.process(imgRGB)
      print(results.multi_hand_landmarks)
      
      
      #cv2.imshow("Hand", results)
      cv2.waitKey(1)
      




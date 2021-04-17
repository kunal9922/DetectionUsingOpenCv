import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(r"dataSet\handTestVideo.mp4")
#import the class  from mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils # -----this method allows us to drawlines on hands

while True:
      success, img = cap.read()
      imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
      results = hands.process(imgRGB)  #           result contains the detected landmarks as dictionary 
      # print(results.multi_hand_landmarks)

      # --- detected the hand 
      if results.multi_hand_landmarks:
            # get the how many hand we detected in an img.
            for handlms in results.multi_hand_landmarks:
                   mpDraw.draw_landmarks(img, handlms, mpHands.HAND_CONNECTIONS)
      
      cv2.imshow("Hand", img)
      cv2.waitKey(1)
      




import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(r"dataSet\handTestVideo.mp4")
#import the class  from mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils # -----this method allows us to drawlines on hands

#show frame rate for showing the CPU performace.
pTime = 0
cTime =  0
while True:
      success, img = cap.read()
      img = cv2.resize(img, (720, 720))
      imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
      results = hands.process(imgRGB)  #           result contains the detected landmarks as dictionary 
      # print(results.multi_hand_landmarks)

      # --- detected the hand 
      if results.multi_hand_landmarks:
            # get the how many hand we detected in an img.
            for handlms in results.multi_hand_landmarks:
                  
                   mpDraw.draw_landmarks(img, handlms, mpHands.HAND_CONNECTIONS)

      #calculate the frame rate framePerSecond fps.
      cTime = time.time()
      fps = 1/(cTime - pTime)
      pTime = cTime
      
      cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)
      cv2.imshow("Hand", img)
      cv2.waitKey(1)
      




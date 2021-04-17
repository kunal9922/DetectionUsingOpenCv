import cv2
import mediapipe as mp
import time

class HandDetector():
      def __init__(self, mode=False, maxHands=2,detectionCon=0.5, trackCon=0.5):
            self.mode = mode
            self.maxHands = maxHands
            self.detectionCon = detectionCon
            self.trackCon = trackCon

            #import the class  from mediapipe
            self.mpHands = mp.solutions.hands
            self.hands = self.mpHands.Hands(self.mode, self.maxHands,
                                                                                          self.detectionCon, self.trackCon)
            self.mpDraw = mp.solutions.drawing_utils # -----this method allows us to drawlines on hands

      def findHands(self, img, draw=True):
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = self.hands.process(imgRGB)  #           result contains the detected landmarks as dictionary 
            # print(results.multi_hand_landmarks)

            # --- detected the hand 
            if results.multi_hand_landmarks:
                  # get the how many hand we detected in an img.
                  for handlms in results.multi_hand_landmarks:
                           if draw:
                                 self.mpDraw.draw_landmarks(img, handlms,
                                                                                                      self.mpHands.HAND_CONNECTIONS)
            return img
      

def workWithHandsDetect():
      pTime = 0
      cTime = 0
      # create a detector for detect the hands landmarks
      handsDetector = HandDetector()
      
      cap = cv2.VideoCapture(r"dataSet\handTestVideo.mp4")
      while cap.isOpened():
            success, img = cap.read()
            img = handsDetector.findHands(img)

            #calculate the frame rate framePerSecond fps.
            cTime = time.time()
            fps = 1/(cTime - pTime)
            pTime = cTime

            cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)
            cv2.imshow("Hand", img)
            cv2.waitKey(1)
            
            
workWithHandsDetect()

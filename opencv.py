import cv2 
from playsound import playsound
#import numpy as np
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(1) 
detector = HandDetector(detectionCon = 0.3, maxHands = 2)

cap.set(3,1152)
cap.set(4,560)
cap.set(10,100)
x = 1000

while True:

    success, img = cap.read() #reads the input image from the webcam
    hands, img = detector.findHands(img) #from input image it detects the hands
    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"] #List of 21 Landmarks points
        bbox1 = hand1["bbox"] #Bounding box info (x,y,w,h) where x,y are coordinates and w,h are width and height
        centerPoint1 = hand1["center"] #center of the hand cx,cy
        handType1 = hand1["type"] #Hand Type Left or Right

    if len(hands)==2:
        hand2 = hands[1]
        lmList1 = hand2["lmList"] #List of 21 Landmarks points
        bbox1 = hand2["bbox"] #Bounding box info x,y,w,h
        centerPoint2 = hand2["center"] #center of the hand cx,cy
        handType2 = hand2["type"] #Hand Type Left or Right

        #print(len(lmList1),lmList1)
        #print(bbox1)
    #    print(centerPoint1, centerPoint2)
       
       # print(handType1,handType2)
        length, info, img = detector.findDistance(centerPoint1, centerPoint2, img)
        x = length
        print(length)

    #    print(handType1, handType2)
    #    if x <= 200:
    #       playsound("C:\\Users\\HEET\\Music\\bolna.mp3")
                    
    cv2.imshow("Video", img)  #displaying output image

    if x <= 100:
        playsound("C:\\Users\HEET\\Music\\girls like you.mp3")
              
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

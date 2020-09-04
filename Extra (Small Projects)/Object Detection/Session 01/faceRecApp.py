import cv2
import os
import matplotlib.pyplot as plt
import numpy as np
cap = cv2.VideoCapture(0)

cascade = "cascades/haarcascade_frontalface_alt2.xml"
face_cascade = cv2.CascadeClassifier(cascade)

blue = (155,0,0)
frame_stroke = 2

while True:
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w, h) in faces:
    	roi_gray = gray_frame[y:y+h, x:x+w]
    	roi_color = frame[y:y+h, x:x+w]
    	img_item = 'my-imge.png'
    	cv2.rectangle(frame, (x,y), (x+w, y+h), blue, frame_stroke)
    	#cv2.imwrite(img_item,roi_color)
    
    cv2.imshow("Face REC",frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2,destroyAllWindows()
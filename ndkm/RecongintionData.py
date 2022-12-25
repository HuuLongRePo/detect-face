import cv2
import numpy as np
import os
import sqlite3
from PIL import Image
from pathlib import Path

def get_project_root() -> Path:
    return Path(__file__).parent.parent
pathroot = str(get_project_root())

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
#thuật toán phát hiện khuôn mặt
recognizer = cv2.face.LBPHFaceRecognizer_create()
#Thuật toán nhận diện khuôn mặt LBPs
recognizer.read(pathroot+'/ndkm/recognizer/trainingData.yml')
#đọc file training

def getProfile(id):
    conn = sqlite3.connect(pathroot+'/ndkm/data.db')
    query = 'SELECT * FROM people WHERE ID = ' + str(id)
    cursor = conn.execute(query)
    profile = None
    for row in cursor:
        profile = row
    conn.close()
    return profile

cap = cv2.VideoCapture(0)
fontface = cv2.FONT_HERSHEY_SIMPLEX
#Thêm văn bản vào hình ảnh
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,225),2)
        roi_gray = gray[y:y+h,x:x+w]
        id,confidence = recognizer.predict(roi_gray)
        #recognizer trả về id từ file tranningData và độ tin cậy 
        #Công cụ nhận dạng .predict()trả về chủ sở hữu của khuôn mặt đó, cho biết id và mức độ tin cậy của việc nhận dạng.
        if confidence<40:
            profile = getProfile(id)
            #lấy thông tin từ database 
            if(profile !=None):
                cv2.putText(frame,""+str(profile[1]),(x+10,y+h+30), fontface,1,(0,0,255),2)
                cv2.putText(frame, str(confidence), (x+5,y+h-5), fontface, 1, (255,255,0), 1)  
        else:
            cv2.putText(frame,"Unknown",(x+10,y+h+30), fontface,1,(0,0,255),2)
    cv2.imshow('image',frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()

import cv2
import numpy as np
import sqlite3
import os
from pathlib import Path

def get_project_root() -> Path:
    return Path(__file__).parent.parent
pathroot = str(get_project_root())

def insertOrUpdate(id, name):
    conn = sqlite3.connect(pathroot+'/ndkm/data.db') #connect to database 
    query = "SELECT * FROM people WHERE ID =" + str(id)
    cusror = conn.execute(query)
    #check recode if exist, update it 
    #else insert it 
    isRecordExist = 0
    for row in cusror:
        isRecordExist = 1

    if(isRecordExist ==0):
        query = "INSERT INTO people(ID, Name) VALUES("+str(id)+",'"+str(name)+"')"
    else:
        query = "UPDATE people SET Name = '"+str(name)+"'WHERE ID ="+str(id)

    conn.execute(query)
    conn.commit()
    conn.close()

id = input("Enter your ID: ")
name = input("Enter your Name: ")
insertOrUpdate(id,name)

#nhận diện khuôn mặt với HAAR Cascade trong OpenCV. 
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
#Sử dụng hàm OpenCV CascadeClassifier () bằng cách chuyển tệp XML làm đối số.
cap = cv2.VideoCapture(0)
#Khởi tạo nguồn cấp dữ liệu webcam.

sampleNum = 0
#sampleNum điều kiện dừng chương trình khi > 100. Lấy 100 ảnh 
while(True):
    ret, frame = cap.read()
    # Sử dụng chức năng ‘read ()’ để tìm nạp các khung hình liên tiếp từ nguồn cấp dữ liệu webcam
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #chuyển đổi frame thành thang độ xám (sử dụng cv2.cvtColor)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    #‘detector’, hàm này trả về tọa độ (x, y, w, h) của các khuôn mặt được phát hiện bởi bộ phân loại.
    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
        # ‘cv2 rectangle’ để đặt một khung giới hạn xung quanh khuôn mặt 
        if not os.path.exists("dataSet"):
            #kiểm tra thư mục dataSet "nếu không tồn tại"
            os.makedirs('dataSet')
            #tạo thư mục dataSet bằng makedirs
        sampleNum +=1
        #sampleNum tăng dần để đặt tên cho từng ảnh cho đến khi >100
        cv2.imwrite("dataSet/User."+str(id)+"."+str(sampleNum)+".jpg",gray[y: y+h,x: x+w])
        #imwrite ghi ảnh ra thư mục dataSet với tên là User.<id user>.<sampleNum>.jpg 
        #gray[] 1 khung hình thang độ xám 
    cv2.imshow("frame",frame)
    #hiển thị khung ảnh 
    if cv2.waitKey(1) & 0xFF == 27:
        break
    # chờ 1 mili giây để nhấn phím trên cửa số openCV 
    if sampleNum > 100:
        break
cap.release()
#giải phóng nguồn cấp dữ liệu video webcam đã được tải vào bộ nhớ.
cv2.destroyAllWindows()

        

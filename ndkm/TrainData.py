import cv2
import numpy as np
import os
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
#Thuật toán nhận diện khuôn mặt LBPs
path = 'dataSet'
#Load đường dẫn và file trong thư mục dataSet
def getImageWithId(path):
    imagePaths = [os.path.join(path,f)for f in os.listdir(path)]
    print(imagePaths)
    faces = []
    IDs = []
    for imagePath in imagePaths:
        FaceImg = Image.open(imagePath).convert('L')
        #Convert ảnh hình ảnh chế độ L -> thang độ xám
        FaceNp = np.array(FaceImg,'uint8')
        #Chuyển đổi một hình ảnh thành mảng numpy
        print(FaceNp)
        Id = int(imagePath.split('/')[1].split('.')[1])#window thì split('\\')
        #tách ID từ tên file ảnh
        faces.append(FaceNp)
        IDs.append(Id)
        #add vào mảng faces, add Id vào ID
        cv2.imshow('trainning',FaceNp)
        cv2.waitKey(10)
    return faces,IDs
faces,IDs = getImageWithId(path)
recognizer.train(faces, np.array(IDs))
#Traning 

if not os.path.exists('recognizer'):
    os.makedirs('recognizer')
recognizer.save('recognizer/trainingData.yml')
#lưu vào file
cv2.destroyAllWindows()
    


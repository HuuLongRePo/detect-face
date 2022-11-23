import cv2
import numpy as np
import os
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
path = 'dataSet'
def getImageWithId(path):
    imagePaths = [os.path.join(path,f)for f in os.listdir(path)]
    #print(imagePaths)

    faces = []
    IDs = []
    for imagePath in imagePaths:
        FaceImg = Image.open(imagePath).convert('L')
        FaceNp = np.array(FaceImg,'uint8')
        print(FaceNp)

        Id = int(imagePath.split('\\')[1].split('.')[1])

        faces.append(FaceNp)
        IDs.append(Id)
        cv2.imshow('trainning',FaceNp)
        cv2.waitKey(10)
    return faces,IDs
faces,IDs = getImageWithId(path)
recognizer.train(faces, np.array(IDs))

if not os.path.exists('recognizer'):
    os.makedirs('recognizer')
recognizer.save('recognizer/trainingData.yml')
cv2.destroyAllWindows()
    


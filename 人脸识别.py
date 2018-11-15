#encoding:utf-8

import cv2

filename = "1.jpg"

def detect(filename):
    #haarcascade_frontalface_default.xml存储在package安装的位置
    #face_cascade = cv2.CascadeClassifier("C:\\Users\\czy\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #传递参数是scaleFactor和minNeighbors,分别表示人脸检测过程中每次迭代时图像的压缩率以及每个人脸矩形保留近邻数目的最小值
    #检测结果返回人脸矩形数组
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        #img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        img = cv2.circle(img,(x+w//2,y+h//2),w//2,(255, 0, 0), 2)
        cv2.namedWindow("Human Face Result!")
        cv2.imshow("Human Face Result!", img)
        cv2.imwrite("images/Face.jpg", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        

detect(filename)
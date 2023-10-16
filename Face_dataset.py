import cv2
import numpy as np
import os
cam=cv2.VideoCapture(0)
cam.set(3,640) #width
cam.set(4,480) #height
user_ids = set()
face_detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


face_id=input("\n Enter user id and press enter")
if face_id in user_ids:
    print("User ID already exists. Please try a different ID.")
    exit()
user_ids.add(face_id)
print("\n [INFO] Initializing face capture.")
count=0
while(True):
    ret,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_detector.detectMultiScale(gray,1.1,5)
    
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        count+=1
        cv2.imwrite("Dataset/User."+str(face_id)+'.'+str(count)+".jpg",gray[y:y+h,x:x+w])
        cv2.imshow('image',img)
    k=cv2.waitKey(100) & 0xff
    if k==27:
        break
    elif count>=50:
        break
print("\n [INFO] Exiting program")
cam.release()
cv2.destroyAllWindows()

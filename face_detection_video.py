import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0)

while(True):
    ret,frame=cap.read()
    # grayimg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    faces=face_cascade.detectMultiScale(frame,1.2,4)
    for(x,y,w,h) in faces:
        crop=frame[y:y+h,x:x+w]
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1)==ord('c'):
        break
    
cap.release()  #to avoid stuck
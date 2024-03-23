import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img_cap=cv2.imread('/Users/thushinbhanu/Downloads/Maitexapython/opencv/group-people-working-out-business-plan-office.jpg')

while(True):
    
    # grayimg=cv2.cvtColor(img_cap,cv2.COLOR_BGR2GRAY)
    
    faces=face_cascade.detectMultiScale(img_cap,1.2,2)
    for(x,y,w,h) in faces:
        # crop=img_cap[y:y+h,x:x+w]
        cv2.rectangle(img_cap,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('frame',img_cap)
    if cv2.waitKey(1)==ord('c'):
        break
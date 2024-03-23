import cv2
vid=cv2.VideoCapture('/Users/thushinbhanu/Downloads/IV/IMG_2754.MOV')  #play video
# vid=cv2.VideoCapture(0)  #opens webcam
# vid=cv2.VideoCapture("http://192.168.137.29:4747/video")  #using droidcam connect to mobile camera

from datetime import datetime
while vid.isOpened():
    ctime=datetime.now()
    ret,frame=vid.read()
    if ret==True:
        cv2.putText(frame,str(ctime),(10,100),cv2.FONT_HERSHEY_COMPLEX,3,(100,150,200),5)
        cv2.imshow('video',frame)
    if cv2.waitKey(1)==ord('c'):
        break
   
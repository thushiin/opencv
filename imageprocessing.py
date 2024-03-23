import cv2
img_vec=cv2.imread('/Users/thushinbhanu/Downloads/Maitexapython/opencv/IMG_2119_jpg.JPG')
print(img_vec)

# cv2.imshow('image',img_vec)
# cv2.destroyAllWindows()

img_gray=cv2.cvtColor(img_vec,cv2.COLOR_BGR2GRAY)
img_gray=cv2.resize(img_gray,(400,600))
print(img_gray)

print(img_gray.shape)

c=(100,150,180)
cv2.rectangle(img_gray,(50,10),(350,500),c,9)
cv2.circle(img_gray,(250,200),50,c,7)
cv2.line(img_gray,(100,40),(250,40),c,8)
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img_gray,"Mountain",(100,30),font,1,(255,255,255),1)
cv2.imshow('image',img_gray)

cv2.imwrite('img.jpg',img_gray)


cv2.waitKey(0)
# import cv2
# import os

# video_capture = cv2.VideoCapture(0)
# folder=input("Enter folder name to save image: ")

# face_count = 0
# max_faces = 20

# while face_count < max_faces:
#     ret, frame = video_capture.read()
    
    
#     face_count += 1
#     image_path=os.path.join(folder,f'image_{face_count}.jpg')
#     cv2.imwrite(image_path,frame)        
    

# video_capture.release()
# cv2.destroyAllWindows()

############################################################################################

##take images by clicking s

# import cv2
# import os
# def main():
#     folder=input("Enter folder name to save image: ")
#     if not os.path.exists(folder):
#         os.makedirs(folder)
        
#     cam=cv2.VideoCapture(0)
#     if not cam.isOpened():
#         print('Error: Unable to open camera')
#         return
    
#     image_count=0
#     while True:
#         ret,frame=cam.read()
#         if not ret:
#             print("Error: Unable to capture image")
#             break
#         cv2.imshow('Press "s" to save and "q" to quit',frame)
#         key=cv2.waitKey(1)
        
#         if key==ord('s'):
#             image_count+=1
#             image_path=os.path.join(folder,f'image_{image_count}.jpg')
#             cv2.imwrite(image_path,frame)
#             print(f'Image {image_count} saved')
            
#         elif key==ord('q'):
#             break
        
#     cam.release
    
# main() 

########################################################################################

import cv2
import os

camera = cv2.VideoCapture(0)
folder_name = input("Enter the folder name to save images: ")
num_images = 10

image_count = 0
while image_count < num_images:
    ret, frame = camera.read()
    image_count += 1
    image_path = os.path.join(folder_name, f"image_{image_count}.jpg")
    cv2.imwrite(image_path, frame)
    print(f"Image {image_count} saved.")
print(os.getcwd())


# Release camera and close OpenCV windows
camera.release()
cv2.destroyAllWindows()

####################################################################################################

# import cv2
# import os

# def capture_images(folder_name, num_images_per_person=10, num_persons=2):
#     camera = cv2.VideoCapture(0)

#     for person in range(num_persons):
#         person_folder = os.path.join(folder_name, f"Person_{person+1}")
#         if not os.path.exists(person_folder):
#             os.makedirs(person_folder)

#         for image_count in range(num_images_per_person):
#             ret, frame = camera.read()

#             image_path = os.path.join(person_folder, f"image_{image_count+1}.jpg")
#             cv2.imwrite(image_path, frame)
#             print(f"Image {image_count+1} for Person {person+1} saved.")

#         if person < num_persons - 1:
#             input("Press Enter to continue to the next person...")

#     # Release camera and close OpenCV windows
#     camera.release()
#     cv2.destroyAllWindows()

# def main():
#     folder_name = input("Enter the folder name to save images: ")
#     num_images_per_person = 10  # Adjust as needed
#     num_persons = 3  # Adjust as needed
#     capture_images(folder_name, num_images_per_person, num_persons)

# if __name__ == "__main__":
#     main()
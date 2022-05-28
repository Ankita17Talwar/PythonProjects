# Face Detection
# https://github.com/anaustinbeing/haar-cascade-files  :: to get haarcascade files
import cv2

# 1. create front face cascade classifier
front_face_cascade = cv2.CascadeClassifier("data\Files\haarcascade_frontalface_default.xml")

# 2. read image
img = cv2.imread('data\Files\photo.jpg')

# 3. Gray Scale image : use either way
# grayscale_img = cv2.imread('data\Files\photo.jpg', 0)
grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# sacle factor small value -> more accuracy
front_faces = front_face_cascade.detectMultiScale(grayscale_img, scaleFactor=1.05, minNeighbors=5) 

print(type(front_faces))
print(front_faces)


# add green rectangle with thickness 3 to face
for x,y,w,h in front_faces:
    img = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3)

resized_img = cv2.resize(img, (int(img.shape[1]/3),int(img.shape[0]/3))) # width = number of col, height = rows

# Show image
cv2.imshow('Gray', grayscale_img)
cv2.waitKey(2000)
cv2.imshow('Gray', resized_img)
cv2.imwrite('Output\\resized_frontFace_img.jpg',resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()




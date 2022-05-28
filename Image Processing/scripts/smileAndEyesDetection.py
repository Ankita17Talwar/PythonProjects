import cv2


face_cascade=cv2.CascadeClassifier('data\Files\haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('data\Files\haarcascade_smile.xml')
eyes_cascade = cv2.CascadeClassifier("data\Files\haarcascade_eyes.xml")


img_nm = 'smile2.jpg'
img = cv2.imread('data\\Files\\' + img_nm)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x1, y1, w1, h1) in faces:
    cv2.rectangle(img, (x1, y1), (x1 + w1, y1 + h1), (255, 0, 0), 3)
    face_gray= gray[y1:y1 + h1, x1:x1 + w1]
    face_color = img[y1:y1 + h1, x1:x1 + w1]
    
    smiles = smile_cascade.detectMultiScale(face_gray, 1.3, 15)
    for (x, y , w ,h) in smiles:

        cv2.rectangle(face_color, (x,y), (x+w, y+h), (0, 0 ,255), 3)
    
    eyes = eyes_cascade.detectMultiScale(face_gray, 1.3, 5)
    for x,y,w,h in eyes:
        cv2.rectangle(face_color, (x,y), (x+w, y+h), (0, 255 , 0), 3)

    
cv2.imshow('img', img)
cv2.imwrite('Output\\detect_e_s_' + img_nm, img)
cv2.waitKey(0)


cv2.destroyAllWindows()

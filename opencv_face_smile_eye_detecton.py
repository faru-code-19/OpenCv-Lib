import cv2 



face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #face detection
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml') #eye detection
smile_cascade=cv2.CascadeClassifier('haarcascade_smile.xml')    #smile detection

#read the image
img=cv2.imread('abd1.jpg')

#convert to gray scale
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
#draw rectangle around the faces
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)


    # Region of interest (ROI) for eyes inside the face
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]
    
    # Detect eyes inside the face ROI
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)


    #detect smiles in roi_gray (inside face)
    smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.7, minNeighbors=20)
    for (sx, sy, sw, sh) in smiles:
        cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)  # Red for smile




#show the output
cv2.imshow('Face Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
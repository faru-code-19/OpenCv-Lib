import cv2

img=cv2.imread("pic3.png")

cv2.line(img,pt1=(50,50),pt2=(100,30),color=(0,255,0),thickness=2)
cv2.rectangle(img,pt1=(50,50),pt2=(100,30),color=(0,255,0),thickness=2)
cv2.circle(img,center=(200,200),radius=30,color=(0,255,0),thickness=-1)

cv2.imshow("Line on image",img)
cv2.imshow("Line on image",img)
cv2.imshow("Line on image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
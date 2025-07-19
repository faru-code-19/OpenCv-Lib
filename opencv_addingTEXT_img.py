import cv2

img=cv2.imread("pic3.png")

cv2.putText(img,"hi this is a text",(10,300),cv2.FONT_HERSHEY_DUPLEX,2,(34,65,23),2)
cv2.imshow("text add",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
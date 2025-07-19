import cv2

#load img
img=cv2.imread("pic1.png")

#show img
cv2.imshow("window 1",img)
cv2.waitKey(0)

#save img
cv2.imwrite("saved_pic1.jpg",img)

#close windows
cv2.destroyAllWindows()

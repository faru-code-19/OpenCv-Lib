import cv2

img=cv2.imread('pic5.jpg',cv2.IMREAD_GRAYSCALE)

blurred=cv2.GaussianBlur(img,(3,3),2)

edges=cv2.Canny(blurred,100,200) 

cv2.imshow("original",img)
cv2.imshow("edges",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
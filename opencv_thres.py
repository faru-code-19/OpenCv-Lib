import cv2

img=cv2.imread('pic5.jpg',cv2.IMREAD_GRAYSCALE)

ret,thres=cv2.threshold(img,100,255,cv2.THRESH_BINARY)
cv2.imshow("original",img)
cv2.imshow("edges",thres)
cv2.waitKey(0)
cv2.destroyAllWindows()
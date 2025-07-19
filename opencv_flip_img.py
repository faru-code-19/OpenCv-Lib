import cv2

img=cv2.imread("pic3.png")

flip_img1=cv2.flip(img,0)
flip_img2=cv2.flip(img,1)
flip_img3=cv2.flip(img,-1)

cv2.imshow("img 0",flip_img1)
cv2.imshow("img 1",flip_img2)
cv2.imshow("img -1",flip_img3)

cv2.waitKey(0)
cv2.destroyAllWindows()
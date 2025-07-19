import cv2

img=cv2.imread("pic3.png")

rotated_img1=cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
rotated_img2=cv2.rotate(img,cv2.ROTATE_180)
rotated_img3=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("window1",rotated_img1)
cv2.imshow("window2",rotated_img2)
cv2.imshow("window3",rotated_img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
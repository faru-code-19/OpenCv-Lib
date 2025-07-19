import cv2

img=cv2.imread("pic3.png")

(h,w)=img.shape[:2]
center=(w//2,h//2)
angle=33
scale=1.0

M=cv2.getRotationMatrix2D(center,angle,scale)

rot_img=cv2.warpAffine(img,M,(w,h))

cv2.imshow("orignial img",img)
cv2.imshow("rotated img",rot_img)

cv2.waitKey(0)
cv2.imwrite("roated_33_deg_img.png",rot_img)
cv2.destroyAllWindows()

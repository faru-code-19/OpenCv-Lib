import cv2

img=cv2.imread("pic1.png")
if img is not None:
    print("img found")
    cv2.imshow("window1",img) #display img
    cv2.waitKey(0)
    print(img.shape) #display H W C
else:
    print("img not found")

cv2.destroyAllWindows()
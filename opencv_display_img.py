import cv2

#load img
img=cv2.imread("pic1.png")
if img is not None:
    print("image found")
    cv2.imshow("Sql",img) #display img
    cv2.waitKey(0) 
    cv2.destroyAllWindows() 
else:
    print("img not found")
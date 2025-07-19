import cv2

#load img
img=cv2.imread("pic2.png")
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#display img
cv2.imshow("Grey Image",grey)
cv2.waitKey(0)
print(img.shape) #shape of color img
print(grey.shape) #shape of greyscale img

cv2.imwrite("saved_greyscale_img.png",grey)

#destroy all windows
cv2.destroyAllWindows()
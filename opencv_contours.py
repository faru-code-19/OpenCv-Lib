import cv2
#load image
img=cv2.imread('pic8.png')

#convert to grayscale
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#threshold the image
_, thresh= cv2.threshold(gray,120,255,cv2.THRESH_BINARY)

#find contours
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

#draw contours
cv2.drawContours(img,contours,-1,(0,255,0),3)

cv2.imshow('Contours', img)
cv2.waitKey(0)  
cv2.destroyAllWindows()

# Save the output image with contours
cv2.imwrite('contours_saved_img.jpg',img)
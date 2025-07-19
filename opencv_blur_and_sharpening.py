import cv2 
import numpy as np
img=cv2.imread('pic5.jpg')

#blurred=cv2.GaussianBlur(img,(5,5),3)
#blurred=cv2.medianBlur(img,9)




# Sharpening kernel
kernel = np.array([[0, -1,  0],
                   [-1, 5, -1],
                   [0, -1,  0]])

# Apply sharpening
sharp=cv2.filter2D(img,-1,kernel)

cv2.imshow('orginal',img)
#cv2.imshow('blurr img',blurred)
cv2.imshow('blurr img',sharp)

cv2.waitKey(0)
cv2.destroyAllWindows()

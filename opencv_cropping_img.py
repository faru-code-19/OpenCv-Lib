import cv2

# Load the image
img = cv2.imread("pic3.png")

# Crop the image using slicing
cropped_img = img[100:200, 200:300]

# Display the cropped image
cv2.imshow("Cropped Image", cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Optionally, save the cropped image
cv2.imwrite("cropped.jpg", cropped_img)

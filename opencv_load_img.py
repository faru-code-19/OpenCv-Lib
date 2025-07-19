import cv2

# Load image
img = cv2.imread('pic1.png')

if img is None:
    print("image not found")
else:
    print("img found")


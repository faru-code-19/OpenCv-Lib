import cv2

img = cv2.imread("pic1.png")

# Show two image windows
cv2.imshow("Window1", img)
cv2.imshow("Window2", img)

# Wait for a key press
cv2.waitKey(0)

# Close only Window1
cv2.destroyWindow("Window1")

# Wait again to see the other window
cv2.waitKey(0)

# Close the remaining window
cv2.destroyAllWindows()

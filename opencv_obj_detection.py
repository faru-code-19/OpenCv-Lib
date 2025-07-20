import cv2

# Step 1: Read the image
img = cv2.imread("pic12.jpg")
img_copy = img.copy()  # Keep a copy for drawing

# Step 2: Convert to Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Step 3: Thresholding to get binary image
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Step 4: Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Step 5: Loop through contours
for cnt in contours:
    # Step 5.1: Simplify contour using approxPolyDP
    epsilon = 0.02 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)

    # Step 5.2: Draw simplified contour
    cv2.drawContours(img_copy, [approx], 0, (0, 255, 0), 2)

    # Step 5.3: Shape detection
    x, y = approx[0][0]  # get coordinate to write shape name

    if len(approx) == 3:
        shape = "Triangle"
    elif len(approx) == 4:
        shape = "Rectangle"
    elif len(approx) > 4:
        shape = "Circle/Polygon/Oval"
    else:
        shape = "Unknown"

    # Label the shape
    cv2.putText(img_copy, shape, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

# Step 6: Show the result
cv2.imshow("Detected Shapes", img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()

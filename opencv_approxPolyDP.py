import cv2

img = cv2.imread("pic10.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    epsilon = 0.02 * cv2.arcLength(cnt, True)  # 2% of the contour perimeter
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)

cv2.imshow("Simplified Contour", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

cap = cv2.VideoCapture(0)  # 0 = default webcam

while True:
    success, frame = cap.read()  # Read frame
    if not success:
        break

    cv2.imshow("Webcam", frame)  # Show the frame

    if cv2.waitKey(1)== ord('q'):  # Press 'q' to quit
        break

cap.release()           # Release the webcam
cv2.destroyAllWindows() # Close all windows

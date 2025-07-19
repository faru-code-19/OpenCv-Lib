import cv2

cap = cv2.VideoCapture(0)

codec = cv2.VideoWriter_fourcc(*'mp4v') #Sets the codec used to compress the video (mp4 format)
out = cv2.VideoWriter('my_video.mp4', codec, 20.0, (640, 480)) #Creates a new video file with name, codec, FPS, and resolution

while True:
    ret, frame = cap.read()
    if not ret:
        break

    out.write(frame) # Saves the current frame to the video file
    cv2.imshow('Recording MP4', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

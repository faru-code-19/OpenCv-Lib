import cv2

#load img
image=cv2.imread("pic3.png")

if image is not None:
    print("image found")
    cv2.imshow("original image",image) #show original img
    cv2.waitKey(0)
    resize=cv2.resize(image,(200,200)) #resizing the original img
    cv2.imshow("resized image",resize) #show resized img
    cv2.waitKey(0)

    cv2.imwrite("saved_resized_img.png",resize) #saves resized img
else:
    print("img not found")

cv2.destroyAllWindows() #close all windows
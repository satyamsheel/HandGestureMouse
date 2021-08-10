import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 720)


while True:
    # 1. Find hand Landmarks
    success, img = cap.read()
    cv2.imshow("Image", img)
    cv2.waitKey(1)
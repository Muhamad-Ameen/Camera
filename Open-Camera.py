# Just for learning

import cv2

cap = cv2.VideoCapture(0)


def camera():
    while True:
        success, img = cap.read()
        cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)
        cv2.imshow('Muhamad Ameen', img)
        if cv2.waitKey(1) & 0xff == ord('M'):
            break


camera()

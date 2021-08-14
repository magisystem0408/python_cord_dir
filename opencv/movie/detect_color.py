# 色検出


import cv2
import numpy as np


cap =cv2.VideoCapture(1)

while True:
    cv2.namedWindow("img",cv2.WINDOW_NORMAL)
    cv2.resizeWindow("img",540,480)

    ret,frame =cap.read()

    if ret ==False:
        break

    # bgrからhsvに変換
    hsv =cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

# 閾値を定義
    lower =np.array([20,50,50])
    upper =np.array([20,255,255])
    frame_mask =cv2.inRange(hsv,lower,upper)

    # 黄色だけが抽出されるようになる
    dst =cv2.bitwise_and(frame,frame,mask=frame_mask)

    cv2.imshow("img",dst)

    if cv2.waitKey(10)==27:
        break
cv2.destoryAllWindows()
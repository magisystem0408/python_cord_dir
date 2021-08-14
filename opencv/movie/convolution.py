import cv2
import numpy as np

# 全ての値が1/9となるフィルターを用意している
# kernel =np.ones((3,3))/9.0

# 微分フィルター
kernel2 = np.zeros((3, 3))
kernel2[0,0]=1
kernel2[1,0]=2
kernel2[2,0]=1
kernel2[0,2]=-1
kernel2[1,2]=-2
kernel2[2,2]=-1


cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    conbution = cv2.filter2D(frame, -1, kernel2)
    cv2.imshow("Convolution", conbution)
    # cv2.imshow("test", frame)

    if cv2.waitKey(10) == 27:
        break
cv2.destoryAllWindows()

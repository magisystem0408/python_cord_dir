"""
映像の出力保存
"""

import cv2

cap = cv2.VideoCapture(1)

# retは正しく読み込めたらboolで返される
ret, frame = cap.read()

# フレームを取得
# スライスするのはframeが[y][x][color]で格納されているので
h, w = frame.shape[:2]

fourcc = cv2.VideoWriter_fourcc(*"XVID")
dst = cv2.VideoWriter("output/test.avi", fourcc, 30.0, (w, h))

while True:
    ret, frame = cap.read()

    if ret == False:
        break
    cv2.imshow("img", frame)

    dst.write(frame)
    if cv2.waitKey(30) == 27:
        break

cv2.destroyAllWindows()

# メモリ開放
cap.release()

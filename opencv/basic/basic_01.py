import cv2
import os

img =cv2.imread("test.jpg")

cv2.imshow("img",img)

# 画像の出力
os.mkdir("output")
cv2.imwrite("output/test.jpg",img)


# キーボードの入力を受け付ける、押されたキーボードを格納する
#　0は押されるまでずっと待ち続けるという意味
cv2.waitKey(0)
cv2.destroyAllwindows()


"""
画像のリサイズを許すようになる
"""

import cv2

img = cv2.imread("output/test.jpg")
cv2.namedWindow("window", cv2.WINDOW_AUTOSIZE)

cv2.imshow("window", img)

cv2.waitKey(0)
cv2.destroyWindows()

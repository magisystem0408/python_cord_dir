"""
オプティカルフローとは特徴点を見つけて
追いかけていく画像処理
"""
import cv2

cv2.namedWindow("img",cv2.WINDOW_NORMAL)
cv2.resizeWindow("img",1200,800)

# 500点検出する
COUNT =500

# オプティカルフローの収束領域
#　もしくは動かなくなったら収束
criteria =(cv2.TERM_CRITERIA_MAX_ITER | cv2.TERM_CRITERIA_EPS,20,0.03)

# ピラミッドの探索窓
#　画像を荒くしてそこから特徴点をトレースする
lk_params =dict(winSize=(10,10),maxLevel=4,criteria=criteria)

cap =cv2.VideoCapture(1)
ret,frame =cap.read()

# 前の画像を入れる
frame_pre =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

while True:
    ret,frame =cap.read()
    if ret ==False:
        break
    frame_now =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    feture_pre =cv2.goodFeaturesToTrack(frame_pre,COUNT,0.001,5)

    if feture_pre is None:
        continue

    feture_now,status,err =cv2.calcOpticalFlowPyrLK(frame_pre,frame_now,feture_pre,None,**lk_params)
    for i in range(COUNT):
        pre_x =feture_pre[i][0][0]
        pre_y =feture_pre[i][0][1]
        now_x =feture_now[i][0][0]
        now_y =feture_now[i][0][1]
        cv2.line(frame,(pre_x,pre_y),(now_x,now_y),(255,0,0),3)
    cv2.imshow("img",frame)

    frame_pre =frame_now.copy()

    if cv2.waitKey(10)==27:
        break
cv2.destoryAllWindows()


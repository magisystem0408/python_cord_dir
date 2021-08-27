import cv2
"""
画像を比較する

手法として画像をヒストグラム化してそのHISTを比較すれば良い
"""

sample =cv2.imread("img01.jpeg")
sample2 =cv2.imread("img02.jpeg")
sample3 =cv2.imread("img03.jpeg")



# 正規化する(リサイz)
img_size=(300,300)
s01_resize=cv2.resize(sample,img_size)
s02_resize=cv2.resize(sample2,img_size)
s03_resize=cv2.resize(sample3,img_size)


# ヒストグラム化
s01_hist=cv2.calcHist(s01_resize,[0],None,[256],[0,256])
s02_hist=cv2.calcHist(s01_resize,[0],None,[256],[0,256])
s03_hist=cv2.calcHist(s01_resize,[0],None,[256],[0,256])



# 画像を比較する
# 第三引数はmethodを入れる(数字を指定してあげれば良い)
result1_2 =cv2.compareHist(s01_hist,s02_hist,1)





print(result1_2)

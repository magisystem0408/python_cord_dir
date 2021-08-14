
# inputの使い方

while True:
    word =input('ここに入力してください')
    if word =='ok':
        #okの文字列を入れると処理を抜ける
        break
    # ok以外のものを入力した場合こっち
    print('next')

# 数字を入れるときは型変換をする必要がある

while True:
    word =input('入力してください')
    # intに型変換
    num =int(word)
    if num==100:
        break
    print('next')

# for文の使い方

# 基本系

some_list =[1,2,3,4,5]

# 反復処理をするものをイテレータと呼ぶ
for i in some_list:
    print(i)

for s in 'abcde':
    print(s)
#実行結果
# a
# b
# c
# d
# e

for s in ['mamushi','timi']:
    if s =='timi':
        # break文もcontinueも組み込める
        break
    print(s)

# 実行結果
# mamushi
# timi

# for-else文
#breakで抜けなればelseを通る
for fruit in ['timi','mamushi','neko']:
    print(fruit)
else:
    print('for文が全て通った場合elseが実行される')

# range関数

# 0から9までを出力してくれる
for i in range(10):
    print(i)

#2から10までを出力してくれる
for i in range(2,10):
    print(i)

#n個飛ばしをしたい場合、3番目の引数に指定する。
for i in range(2,10,3):
    print(i)

# for文の中で変数を使わない場合、アンダースコアで指定する
for _ in range(10):
    print('hello')

# enumerate関数はインデックスを使いたい時に使用する
for i, fruit in enumerate(['timi','mamushi','neko']):
    print(i,fruit)

# 実行結果
# 0 timi
# 1 mamushi
# 2 neko

# zip関数
days =['Mon','Tue','Wed']
fruits = ['apple','mamushi','banana']
drinks =['coffe','tea','beer']

# zipでかくと
for day,fruit,drink in zip(days,fruits,drinks):
    print(day,fruit,drink)

# zipで書かない場合
for i in range(len(days)):
    print(days[i],fruits[i],drinks[i])

# 実行結果
# Mon apple coffe
# Tue mamushi tea
# Wed banana beer


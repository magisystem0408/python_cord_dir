# 初期に読み込まれるファイルが__init__ファイル
# __init__.pyは付け加えないといけない

# インポートの仕方
# import ディレクトリの名前.ファイルの名前

import exermodule.utiles

# 関数の実行
r = exermodule.utiles.say_twice('mamushi')


# fromで書くとコード記述量が少なくなる
from exermodule import utiles

r =utiles.say_twice('mamushi')

# 関数だけをインポートしたい時
# 直し、わかりずらくなるため非推奨
from exermodule.utiles import say_twice
r =say_twice('mamushi')



# import に*を入れると__init__が読み込まれる
#わかりずらいので非推奨
from exermodule.exerpath import *
print(human.sing())


# 組み込み関数

ranking={
    'A':100,
    'B':85,
    'C':95
}

# キーで並べ替え
print(sorted(ranking))

# 実行結果
# ['A', 'B', 'C']

# バリューで並べ替えするとき
# ※低いもの順に並べ替え
print(sorted(ranking,key=ranking.get))
# 実行結果
# ['B', 'C', 'A']

print(sorted(ranking,key=ranking.get,reverse=True))
# 実行結果
# ['A', 'C', 'B']


# 標準モジュール

# 以下の文字列にある文字が入っているかカウントするには
s='jfapihfweihf]afojd]saf'

d={}
for c in s:
    # cというキーがなかったら0を代入する
    d.setdefault(c,0)
    d[c] +=1
print(d)

# 実行結果
# {'j': 2, 'f': 5, 'a': 3, 'p': 1, 'i': 2, 'h': 2, 'w': 1, 'e': 1, ']': 2, 'o': 1, 'd': 1, 's': 1}


# さらにもっと簡単に書くには
from collections import defaultdict

d=defaultdict(int)

for c in s:
    d[c] +=1
print(d)


# 他の人が書いた関数がインポートされてしまう可能性があるので

def main():
    #実行したい関数をここに書く
    print('実行したいもの')

if __name__ =='__main':
    # ここで実行する
    main()

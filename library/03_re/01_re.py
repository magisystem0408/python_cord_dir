# 複雑な文字列の検索に使う
import re

"""
match() 文字列の先頭で正規表現とマッチするか判定
search() 文字列を操作して、正規表現がどこにマッチするかを調べる
findall() 正規表現にマッチする部分文字列を全て探し出しリストとして返す
finditer() 重複しないマッチオブジェクトのイテレータを返す
"""

# cの前のドットは任意の文字
m=re.match('a.c','abc')

print(m)

# 実行結果
# <re.Match object; span=(0, 3), match='abc'>
# ない場合はnoneを返す

# 中身を見るときは
print(m.group())


m =re.search('a.c','test abc test')
print(m)
# どこの位置に属するか
print(m.span())

# 中身を見るとき
print(m.group())


# 該当箇所全て出したいとき
m =re.findall('a.c','test abc test abc')
print(m)


m =re.finditer('a.c','test abc test abc')
print([w.group() for w in m])

# ?は0回または1回
m=re.match('ab?','abb')
print(m)

# *、アスタリスクは0回以上
m =re.match('ab*','abbb')
print(m)

# +は一回以上
m=re.match('ab+','abbbb')

# {}のなかに数字で回数を指定
m =re.match('a{3}','aaa')


#{2,4}で2から4回
m =re.match('a{2,4}','aaa')

# 集合 aからcまでの文字が入ってきたらヒットする
m =re.match('[a-c]','x')

# 全てのアルファベットと全ての数字、_をヒットさせるときは以下のように描く
m=re.match('[a-zA-z0-9_]','_')

# 任意の英数文字とマッチするは\wで表現する
m =re.match('\w','a')

# 英数文字意外にしたいときはWを大文字にする
m =re.match('\W','a')
# ↑と一緒にしたいとき
m=re.match('[^a-zA-z0-9_]','_')


# 0から9までは以下の2通りでかける
m =re.match('[0-9]','1')
m =re.match('\d','1')

# ↑否定するには、つまり数字以外とするには、大文字にする

m =re.match('\D','a')

# またはを使うときは、パーテーションを使う
m=re.match('a|b','x')
print(m)

# 塊を一回以上とするとき
m=re.match('(abc)+','abcabc')

# スペースをヒットさせるとき
m =re.match('\s','1')

# 空白文字ではない否定をかける場合
m=re.match('\S',1)

# 特殊文字のヒットさせるやつはバックスラッシュを入れてあげる
m =re.match('\*','*')

# 先頭がabcから
m=re.match('^abc','abctest')

# 最後の文字がヒット
m=re.match('abc$','abctest abc')


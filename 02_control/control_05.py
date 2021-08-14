"""
・ジェネレーター
・内包表記について
"""

# ジェネレーター
# yield を見るとジェネレーターとして判別される

def greeting():
    yield 'Good morning'
    # ここに重たい処理が入ってた時上のyieldは処理をしないで実行できる
    yield 'Good afternoon'
    yield 'Good night'

g =greeting()
print(next(g))
print("mamushi")
print(next(g))
print("mamushi")
print(next(g))

# 実行結果
# Good morning
# mamushi
# Good afternoon
# mamushi
# Good night
# mamushi

# リスト内包表記
t=(1,2,3,4,5)

r=[i for i in t]
print(r)

# 実行結果
# [1, 2, 3, 4, 5]

r=[i for i in t if i%2 ==0]
print(r)

# 実行結果
# [2, 4]


t=(1,2,3,4,5)
t2=(5,6,7,8,9,10)

# 通常で書いた場合
r =[]
for i in t:
    for j in t2:
        r.append(i*j)
print(r)

# 内包表記で書いた場合、これは非推奨
r =[i*j for i in t for j in t2]


# 辞書の内包表記
w=['mon','tue','wed']
f=['coffee','milk','water']

# 通常で書いた場合
d={}
for  x,y in zip(w,f):
    d[x]=y
print(d)

#一行で書いた場合
d ={x:y for x,y in zip(w,f)}
print(d)

# 集合の内包表記
s =set()

# 通常で書いた場合
for i in range(10):
    if i % 2==0:
        s.add(i)
print(s)

#内包表記で書いた場合
s={i for i in  range(10) if i%2 ==0}
print(s)

# ジェネレーター内包表記
def g():
    for i in range(10):
        yield i

g =g()

# これを内包表記すると以下になる
# 括弧になる
g =(i for i in range(10))


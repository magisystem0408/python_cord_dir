# dict型をforで処理をしていく
d ={'x':100,'y':200}

# キーだけを取得したい場合
for v in d:
    print(v)

# 実行結果
# x
# y

#キーとバリューを取得したい場合
#タプルでアンパッキングを使用している

for k,v in d.items():
    print(k,v)

# 実行結果
# x 100
# y 200

# 関数定義

# 基本形
def say_something():
    print ('mamushi')

# 実行
say_something()

# 型を指定して関数定義ができる
def add_num(a:int,b:int) ->int:
    return a+b

# 関数に突っ込む時に位置がズレていた場合
def menu(entree,drink,dessert):
    print(entree)
    print(drink)
    print(dessert)

# 引数を指定して入れてあげる
menu(entree='beef',dessert='ice',drink='beer')

# デフォルト引数はリストで与えないように注意する

def test_func(x,l=None):
    if l is None:
        l=[]
    l.append(x)
    return l
r =test_func(100)

# 実行結果
# [100]

# 引数をまとめて書きたい時
# *argsと書くとまとめられ、実行結果はタプルにまとめてくれる
def say_something(*args):
    print(args)

say_something('mamushi','timi','neko')

# 実行結果
# ('mamushi', 'timi', 'neko')

# 合わせ技
def say_something(*args):
    for arg in args:
        print(arg)

say_something('mamushi', 'timi', 'neko')

# 実行結果
# mamushi
# timi
# neko

# 実際には1引数目は普通に定義する
#1つめは必須で残りには何個入ってくるかわからない場合argsでまとめる

def say_something(word,*args):
    for arg in args:
        print(arg)

t=('timi','mamushi')
say_something('mamushi', *t)


# キーワード引数の辞書化

def memu(**kwargs):
    print(kwargs)

memu(entree='beef',drink='coffee')

# 実行結果
# {'entree': 'beef', 'drink': 'coffee'}


# 辞書(dict)をまとめて関数の中に入れることができる
def memu(**kwargs):
    for k,v in kwargs.items():
        print(k,v)
d={
    'entree':'beef',
    'drink':'ice coffee',
    'dessert':'ice',
}
memu(**d)

# 実行結果
# entree beef
# drink ice coffee
# dessert ice

# 最終形態
def menu(food,*args,**kwargs):
    print(food)
    print(args)
    print(kwargs)

menu('banana','apple','orange',entree='beef',drink='coffee')

# 実行結果
# banana
# ('apple', 'orange')
# {'entree': 'beef', 'drink': 'coffee'}
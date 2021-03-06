d={'x':10,
   'y':20
   }

# 配列の中に特定のキーが入ってますかの判定をしたい時
'特定したいキー' in d

# 実行結果はBoolean

# 追加したい時
d['z']=200
d[1]=10000

# 実行結果
# {'x': 10, 'y': 20, 'z': 200, 1: 10000}

# 以下のようにも定義することが可能
dict(a=10,b=20)



# キーだけ取り出したい場合
d.keys()

# 実行結果
# dict_keys(['x', 'y', 'z', 1])

# バリューだけ取り出したい場合
d.values()

# 実行結果
# dict_values([10, 20, 200, 10000])

# キーを指定して特定のバリューだけ取り出したい時
# 取り出して元々のdictを変更しない方法
d.get('ここでキーを指定する')
# 取り出して元々のdictを削除する方法
d.pop('ここでキーを指定する')



# dictで上書きしたい時
# dをd2でオーバーライドする

d={'x':10,
   'y':20
   }

d2={
    'x':1000,
    'j':500
}

d.update(d2)

# 実行結果
# {'x': 1000, 'y': 20, 'j': 500}

# 辞書型のコピー
# 以下のように記述すると参照元の値まで変化してしまう
x={'a':1}
y=x
y['a']=1000

# これを避けるためにはcopyメソッドを使用する

x={'a':1}
y=x.copy()
y['a']=1000
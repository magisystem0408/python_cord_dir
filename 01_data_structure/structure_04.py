# 集合型
# dict型と集合型は{}で同じなので型を調べるとset()で算出される

a={1,2,2,4,5,6,4,}
print(a)
# 実行結果は2など重複してたものが消えるようになる
# {1, 2, 4, 5, 6}

# 引き算をした時
b={1,2,4}
print(a-b)

# 実行結果は1,2,4が引かれて結果が残る
# {5, 6}


# aかつbで存在してる時
print(a&b)
# 実行結果は共通しているものが取り出される
# {1, 2, 4}

#aまたはbの時
print(a|b)
# aかbに存在しているが、重複はしていないもの
print(a^b)


# また配列ではないので以下はエラーが出てくる
a[0]

# 集合に追加したい時
a.add(6)

# 削除したい時
a.remove('削除したいやつ')


# 使い所は、取得したものからユニークなものをとり出していく
f=['apple','banana','apple','banana']
# 集合からset(集合型)に変換してあげる
kind= set(f)

# 実行結果
# {'apple', 'banana'}

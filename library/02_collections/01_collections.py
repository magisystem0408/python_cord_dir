import collections

a = {'a': 'a', 'c': 'c', 'num': 0}
b = {'b': 'b', 'c': 'cc'}
c = {'b': 'bbb', 'c': 'ccc'}

# 以下のようにaをアップデートすると
# aが上書きされてしまう
print(a)
a.update(a)

print(a)
a.update(c)

print(a)


# これをもっと便利に書くには

m =collections.ChainMap(a,b,c)

print(m)
print(m.maps)

# 逆転させたいとき
m.maps.reverse()
print(m.maps)

print(m['c'])

# 追加したいとき
m.maps.insert(0,{'c':'cccccccc'})
print(m.maps)

# 削除したいとき
del m.maps[0]
print(m.maps)

print(m['c'])


# aのnumに0より小さかった場合に値を入れないで無視するもできる

class DeepChainMap(collections.ChainMap):
    def __setitem__(self, key, value):
        for mapping in self.maps:
            if type(mapping[key])is int and mapping[key] <value:
                mapping[key] =value
            return
        self.maps[0][key] =value


m =DeepChainMap(a,b,c)
m['num']=-1
print(m['num'])
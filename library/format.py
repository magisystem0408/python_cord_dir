
# 基本部分
print('{0},{1},{2}'.format('a','b','c'))
print('{name}{family}'.format(name='timi',family='mamsuhi'))

t=(1,2,3)
print('{t[0] t[2]}'.format(t=t))

# タプルアンパッキング
print('{0}{2}'.format(*t))


d={'name':'jun','famiry':'sakai'}
print('{name}{famiry}'.format(**d))


# 左に30文字追加する
print('{:>30}'.format('right'))

# 真ん中にもって行きたいとき
print('{:^30}'.format('center'))

# 0はインデックスという意味
# スペースをアスタリスクで入れる場合

print('{0:*^30}'.format('center'))
print('{name:*^30}'.format(name ='center'))

# わかりずらいとき
print('{name:{fill}{align}{width}}'.format(name='center',fill='*',align='^',width=30))

# 数字関連を操作するとき
print('{:,}'.format(123456789))

# +を明示的に表示したいとき
print('{:+f}{:+f}'.format(3.14,-3.14))


# 割った後の%表記
print('{:.2%}'.format(3.14,-3.14))


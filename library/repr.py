""":
reprはpythonオブジェクトとして表示される
"""

print('s')
print(str('s'))
print(repr('s'))

# 実行結果
# s
# s
# 's'

# printのなかに、reprを描きたい場合
print('{!r}{}{}'.format('test','test1','test2'))


"""
pprintとjsonについて
"""


import json
import pprint

l =['a','b','c']
l.insert(0,l[:])

# リストの中にリストなどがあるとき
# [['a', 'b', 'c'], 'a', 'b', 'c']

#表示するときの操作を可能にするのがPrettyprinter
pp =pprint.PrettyPrinter(indent=4)
pp.pprint(l)

# わかりやすく表示ができる


d={'a':'A','b':'B','c':'C','d':{'x':{'y':'Y'}}}

#indentでわかりやすく表示できる
print(json.dumps(d,indent=4))


# 実行結果
# {
#     "a": "A",
#     "b": "B",
#     "c": "C",
#     "d": {
#         "x": {
#             "y": "Y"
#         }
#     }
# }



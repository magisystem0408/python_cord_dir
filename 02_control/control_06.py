"""
・エラーハンドリング try-except
・独自エラー作成について

"""

# スコープについて
animal ='cat'

def f():
    #グローバル変数を使用したい時はこのようにする
    global animal
    animal = 'dog'
    print('local',animal)
    # 以下でスコープが確認できるようになる
    print(locals())


# エラーハンドリング
# try-except
l=[1,2,3]
i=5

try:
    l[i]
except:
    print("Don't worry")

# IndexErrorが起きた時だけexceptにする
try:
    l[i]
except IndexError as ex:
    print("Don't worry:{}".format(ex))
except NameError as ex:
    print(ex)
else:
    print('上のexceptで何も問題なく抜けた場合に実行される')
finally:
    print('最後に必ずこの行が実行される')


# 自作例外を作るには
raise IndexError('自作エラーが作成可能')

# 実用例

# 独自エラー作成
class UppercaseErrpr(Exception):
    pass


def check():
    words =['APPLE','mamushi','timitimi']
    for word in words:
        if word.isupper():
            raise UppercaseErrpr(word)

try:
    check()
except UppercaseErrpr as exc:
    print('これは私の間違え次に言ってください')

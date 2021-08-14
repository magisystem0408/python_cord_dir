# まずデコレーターの一部である
import contextlib

# デコレータの復習
def tag(f):
    def _wrapper(content):
        print('<h2>')
        r =f(content)
        print('</h2>')
        return r
    return _wrapper

# @tag
# def f():
#     print('test')

# @を使用しないで書く場合
def f(content):
    print(content)

# これを実行するときは
# return _wrapperで()無いのでまだ実行されていない

f =tag(f)

# ここで初めて実行される
f('timi')


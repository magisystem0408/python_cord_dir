# デコレーターに引数を渡して
#　渡した先で使用したい場合に使用する

import contextlib

# 普通に書いた場合
def tag(name):
    def _tag(f):
        def _wrapper(content):
            print('<{}>'.format(name))
            r =f(content)
            print('</{}>'.format(name))
        return _wrapper
    return _tag

@tag('h2')
def f(content):
    print(content)

f('test')



@contextlib.contextmanager
def tag(name):
    print('<{}>'.format(name))
    yield
    print('</{}>'.format(name))


# @tag('mamushi')
# def f(content):
#     print(content)
#
# f('test')

# withステートメントで書くと簡略化できる
with tag('neko'):
    print('test')

print()
# 応用例「ネストで実行される」

def f():
    print('ネストで実行される')
    with tag('nesuto'):
        print('#########ああああ')
        with tag('neko'):
            print('nekoneko')
f()


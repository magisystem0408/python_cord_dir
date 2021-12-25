def s_hello():
    yield "hello1"
    yield "hello2"
    yield "hello3"

    # 4回目を読んだときにNoneが帰ってきてしまう。
    # returnを入れるとdoneが帰ってくる
    return "done"

def g_hello():
    while True:
        r =yield from s_hello()
        yield r


g =g_hello()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

#  実行結果
# hello1
# hello2
# hello3
# done
# hello1
# hello2
# hello3
# done
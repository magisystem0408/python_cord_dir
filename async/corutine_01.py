"""ジェネレーターのcorutine"""

def g_hello():
    while True:
        r = yield "hello"
        yield r

g = g_hello()
print(next(g))

# ジェネレーターにplusを送る
print(g.send("mamushi"))
print(next(g))
print(g.send("nancy"))

# 実行結果
# hello
# mamushi
# hello
# nancy
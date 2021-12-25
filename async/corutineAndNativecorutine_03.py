import asyncio

# ループオブジェクト生成
loop = asyncio.get_event_loop()


# デコレーターを必ず書く(これは昔の書き方)
# @asyncio.coroutine

# async-awaitはネイティブのコルーチン
async def worker():
    print("start")
    # yield from asyncio.sleep(2)
    await asyncio.sleep(2)
    print("stop")


if __name__ == '__main__':
    # タスク指定
    loop.run_until_complete(asyncio.wait([worker(), worker()]))
    loop.close()

import asyncio
import time

import aiohttp
import requests

loop = asyncio.get_event_loop()


# async def hello(url):
#     print(requests.get(url).content)
#     print(time.time())


async def hello(url):
    # async with aiohttp.ClientSession() as session:
    #     async with session.get(url) as response:
    #         response =await response.read()
    #         print(response)
    #         print(time.time())
    #  上の処理を簡略化したのが
    await asyncio.sleep(10)


# これは一回目のアクセスが終了してから次のアクセスが始まる
loop.run_until_complete(asyncio.wait([
    hello("http://httpbin.org/headers"),
    hello("http://httpbin.org/headers")]))

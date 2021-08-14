"""
REST

HTTPメソッド・クライアントが行いたい処理をサーバーに伝える

GET     データの参照
POST    データの新規登録
PUT    データの更新
DELET　データの削除

"""

import urllib
import urllib.request
import json

url ='http://httpbin.org/get'


# アクセスするには
with urllib.request.urlopen(url) as f:
    # urf-8でデコードしてあげる
    # jsonでロードしてあげる
    print(json.loads(f.read().decode('utf-8')))

# 実行結果
# ディクショナリー型で返ってくる

# {'args': {}, 'headers': {'Accept-Encoding': 'identity', 'Host': 'httpbin.org', 'User-Agent': 'Python-urllib/3.8', 'X-Amzn-Trace-Id': 'Root=1-60841eba-4c55532458466f58263bdc3d'}, 'origin': '182.170.239.204', 'url': 'http://httpbin.org/get'}


# urlにパラメータを設定したい場合

# getの場合
# getでパラメータ送るときは?をつけて&で繋ぐ

payload ={'key1':'value1','key2':'value2'}

# エンコードはしてあげる必要がある
url ='http://httpbin.org/get' +'?'+urllib.parse.urlencode(payload)
print(url)

# 実行結果
# http://httpbin.org/get?key1=value1&key2=value2


# postで送る場合
payload =json.dumps(payload).encode('utf-8')
req =urllib.request.Request('http://httpbin.org/post',
                            data=payload,method='POST')

with urllib.request.urlopen(url) as f:
    print(json.loads(f.read().decode('utf-8')))


# PuTの場合

req =urllib.request.Request('http://httpbin.org/put',
                            data=payload,method='PUT')

with urllib.request.urlopen(url) as f:
    print(json.loads(f.read().decode('utf-8')))


# デリートの場合

req =urllib.request.Request('http://httpbin.org/delete',
                            data=payload,method='DELETE')

with urllib.request.urlopen(url) as f:
    print(json.loads(f.read().decode('utf-8')))

    
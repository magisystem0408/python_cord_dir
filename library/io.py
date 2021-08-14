import io

# アクセスするときに使う
import requests

import zipfile


# 普通に書いた場合
# with open('/tmp/a.txt','w') as f:
#     f.write('test test')
#
# with open('/tmp/a.txt','r') as f:
#     print(f.read())
#

f =io.StringIO()
f.write('string io test')
# 最初に戻る
f.seek(0)

print(f.read())


# 使用例
# zipfileをダウンロードをメモリ上で処理するときとかに使用する

url ='###########'

f =io.BytesIO()

r =requests.get(url)
f.write(r.content)

with zipfile.ZipFile(f) as z:
    with z.open('ファイル指定') as r:
        print(r.read().decode())
import tarfile

# ファイル圧縮
with  tarfile.open('test.tar.gz','w:gz') as tr:
    tr.add('test_dir')

# ファイル展開
with tarfile.open('test.tar.gz','r:gz') as tr:
    tr.extractall(path='test_tar')


import zipfile


# 書き込み
with zipfile.ZipFile('test.zip','w') as z:
    # フォルダしか作らない
    z.write('test_dir')
    # ファイルを作る
    z.write('test_dir/test.txt')


# 読み込み
with zipfile.ZipFile('test.zip','r') as z:
    z.extract('zzz2')


# ファイルの削除までやってくれる、一次的ファイル
import tempfile
with tempfile.TemporaryFile(mode='w+') as t:
    t.write('hello')
    t.seek(0)
    print(t.read())

# 一時的なディレクトリ版
with tempfile.TemporaryDirectory() as td:
    print(td)

# パス
temp_dir=tempfile.mkdtemp()
print(temp_dir)

# ターミナルで行うことをコードで行う
import subprocess

subprocess.run(['ls'])

# コマンドをつけるには
subprocess.run(['ls','-al'])

# 以下も同様だが非推奨
subprocess.run('ls -al',shell=True)
# だが、|で繋げてコマンドを打ち込むことはできる
subprocess.run('ls -al　|grep test',shell=True)

# 時間関連

import datetime

# 時間表示
now = datetime.datetime.now()

print(now)
# 国際規格のisoフォーマット
print(now.isoformat())

# 時間の表示形式も変えられる
print(now.strftime('%d/%m/%y-%H%M%S%f'))


today =datetime.date.today()
print(today)
print(today.isoformat())
print(today.strftime('%d/%m/%y'))

t =datetime.time(hour=1,minute=10,second=5,microsecond=100)
print(t)
print(t.isoformat())
print(t.strftime('%H_%M_%S_%f'))


# 一週間前

print(now)
d =datetime.timedelta(weeks=-1)
d =datetime.timedelta(days=1)
d =datetime.timedelta(hours=1)
d =datetime.timedelta(minutes=1)
d =datetime.timedelta(second=1)
d =datetime.timedelta(microseconds=1)
print(now+d)


# 一秒間何もしないで待っていたい時
import time
time.sleep(1)

# ファイルのバックアップ

import os
import shutil

file_name ='test.txt'

# バックアップファイルがあるか判定
if os.path.exists(file_name):
    shutil.copy(file_name,"{}.{}".format(
        file_name,now.strftime('%Y_%m_%d_%H_%M_%S')
    ))

with open(file_name,'w') as f:
    f.write('test')

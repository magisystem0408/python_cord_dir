# wは上書き
# aは追加で入る
# rは読み込み
f = open('text.txt','w')
f.write('test')
f.close()

# print関数を使っても書き込める

f = open('test.txt','w')
f.write('Test')
print('I am print', file=f)
f.close()


# withステートメント
#closeはいらなくなる
with open('test.txt','w') as f:
    f.write('test')


# ファイルの読み込み
s ="""mamusj"""


with open('test.txt','r') as f:
    # 一気に読み込み
    print(f.read())

    # 1行ずつ読み込みするには
    while True:
        line = f.readline(5_000_000)
        if not line:
            break

    # 文字ずつ読み込みするには
    while True:
        chunk =2
        line = f.read(chunk)
        print(line)
        if not line:
            break

# seekで読み込むところを移動する
with open('test.txt','r') as f:
    # 居場所を教えてくれる
    print(f.tell())
    print(f.read(1))
    # 移動
    f.seek(5)
    print(f.read(1))


# 書き込んだあと読み込みたい時

s='mamushi'

# wの後に+を追加する
with open('text.txt','w+') as f:
    f.write(s)
    # seekで一番初めに戻って読み込んであげる
    f.seek(0)
    print(f.read())

# 読み込んで書き込みをする場合
# test2.txtが存在しないとエラーになる
with open('test2.txt','r+') as f:
    print(f.read())
    f.seek(0)
    f.read(s)


# テンプレート

import string

s="""
Hi mamushi

$contents
"""

t= string.Template(s)
contents =t.substitute(name='Mike',contents ='neko')
print(contents)

#実行結果
# Hi mamushi
#
# neko

# 他のファイルから読み込みたい時
import string
with open('ここにファイルのパスを書く') as f:
    t=string.Template(f.read())

contents =t.substitute(name='Mike',contents ='neko')
print(contents)

# csvファイルへの書き込みと読み込み
import csv

with open('test.csv','w') as csv_file:
    fieldnames =['Name','Count']
    # csvに書き込むためのオブジェクト生成
    writer =csv.DictWriter(csv_file,fieldnames=fieldnames)
    # ラベル名生成
    writer.writeheader()
    # 書き込む内容生成
    writer.writerow({'Name':'A','Count':1})
    writer.writerow({'Name': 'A', 'Count': 2})

# 読み込み用
with open('test.csv','r') as csv_file:
    reader=csv.DictReader(csv_file)
    for row in reader:
        print(row['Name'],row['Count'])


# ファイルの操作
import os
import pathlib

# 存在しているか
print(os.path.exists('test.txt'))

# これはファイルか？
print(os.path.isfile('test.txt'))

# これはディレクトリか?
print(os.path.isdir('design'))

# リネーム
os.rename('test.txt','新しいファイル名')
os.symlink('renamed.txt','symlink.txt')

# ディレクトリ作成
os.mkdir('ディレクトリ名')
#ディレクトリ削除
os.rmdir('ディレクトリ名')

# pathlibを使用したファイルの作成
pathlib.Path('empty.txt').touch()
# 削除するには
os.remove('empty.txt')


os.mkdir('test_dir')
os.mkdir('test_dir/test_dir2')
# 存在するか確認できるやつ
print(os.listdir('test_dir'))


import  glob
# ファイルが存在するか
print(glob.glob('test_dir/test_dir2/*'))

import shutil
# リネームしてコピーする

shutil.copy('test_dir/test_dir2_empth.txt',
            'test_dir/test_dir2_empth2.txt')

print(glob.glob('test_dir/test_dir2/*'))

# ディレクトリ削除
shutil.rmtree('test_dir')

# 今のディレクトリ位置を知りたい
print(os.getcwd())

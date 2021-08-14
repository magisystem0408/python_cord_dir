import sqlite3


# データベース作成
conn =sqlite3.connect('test_sqlite.db')

# カーソルを定義する
curs = conn.cursor()

# テーブル定美
curs.execute(
    'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)' )

#commitすると書き込まれる
conn.commit()

conn.close()
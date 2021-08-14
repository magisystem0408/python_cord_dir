import sqlite3


# データベース作成
conn =sqlite3.connect('test_sqlite.db')

# カーソルを定義する
curs = conn.cursor()

# テーブル定美
curs.execute('CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)' )

#commitすると書き込まれる
conn.commit()

# カラムを追加する
curs.execute('INSERT INTO persons(name) values("Mike")')
conn.commit()

# カラムの中身をみたいとき

curs.execute('SELECT * FROM persons')
print(curs.fetchall())

# updateで書き換えたいとき
curs.execute('UPDATE persons set name ="Michel" WHERE name="Mike"')
conn.commit()


curs.execute('DELETE FROM persons WHERE name="Mike"')
conn.commit()


# 2つ終了させる
curs.close()
conn.close()


# sql文を何度も実行したり試したりしたいとき
# メモリ上に作成することができる

conn = sqlite3.connect(':memory:')


# mysqlを実行するとき
# ターミナル上で以下のコマンドを実行する

# brew services start mysql

# mysqlにログインするとき
# mysql -u root

# mysqlを止めたいとき
# brew services stop mysql


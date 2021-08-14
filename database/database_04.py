# 簡易的に作りたい時
import dbm

# データベース格納
with dbm.open('cache','c') as db:
    db['key1'] ='value1'
    db['key2'] ='value2'


# データ取り出し
with dbm.open('cache','r') as db:
    print(db.get('key1'))
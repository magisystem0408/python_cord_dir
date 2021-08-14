# コンフィグファイルを作るとき
"""
[DEFAULT]
debug=False

[web_server]
host =127.0.0.1
port =80

[db_server]
host =127.0.0.1
port =3306
"""

import configparser

# 書き込み手順
config = configparser.ConfigParser()
config['DEFAULT'] = {
    'debug': True
}

config['web_server'] = {
    'host':'127.0.0.1',
    'port': 80
}

config['db_server']={
    'host':'127.0.0.1',
    'port':'3306'
}

with open('config.ini','w') as config_file:
    config.write(config_file)


# 読み込み手順

config =configparser.ConfigParser()
config.read('config.ini')

# 読み込みたいコードをprintする
print(config['web_server'])
print(config['web_server']['host'])
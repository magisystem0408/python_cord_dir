"""
以下のようなファイルを作る
ちなみにこの形をブロックタイプという

web_server:
    host:127.0.0.1
    port:80

db_server:
    host:127.0.0.1
    port:3306
"""

import yaml


# 書き込む時
# 第三引数でブロックタイプを指定する

with open('config.yml','w') as yaml_file:
    yaml.dump({
        'web_server':{
            'host':'127.0.0.1',
            'port':80
        },
        'db_server':{
            'host':'127.0.0.1',
            'port':3306
        }
    },yaml_file,default_flow_style=False)


# 読み込む時

with open('config.yml','r') as yaml_file:
    data =yaml.load(yaml_file, yaml.SafeLoader)
    print(data)
    print(data['db_server'])

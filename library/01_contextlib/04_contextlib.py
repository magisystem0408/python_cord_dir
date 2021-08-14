import contextlib

import logging
import sys

# x=input('Enter:')

# inputのレイヤーが低いところでstdinが実行されている
for line in sys.stdin:
    print(line)




print('hello')
sys.stdout.write('hello')
#
#
logging.error('エラーだよん')
sys.stderr.write('エラーだよん')


# 実行結果をファイルに書き込みたい
with open('stdout.log','w') as f:
    with contextlib.redirect_stdout(f):
        print('hello')


# エラーを書き込みたい
with open('stderr','w') as f:
    with contextlib.redirect_stderr(f):
        logging.error('Error')
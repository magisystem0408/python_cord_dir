import logging


# レベル調整をする
# ログファイルを書き出したい場合はfilenameで実行する

logging.basicConfig(
    level=logging.INFO,
    filename='test.log')

logging.critical('critical')
logging.error('error')
logging.warning('warning')
logging.info('critical')
logging.debug('critical')

# %sでformat関数を実行できる

logging.info('info %s' % 'test')

# 複数入れたい場合は、カンマ続きで出せる
logging.info('info %s　％s', 'test', 'test2')


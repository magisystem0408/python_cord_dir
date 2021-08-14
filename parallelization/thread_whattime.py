import logging
import threading
import time

"""
何秒後にスレッドを走らせるか
"""

logging.basicConfig(
    level=logging.DEBUG,
    format='%(threadName)s: %(message)s'
)


def worker1(x,y=1):
    logging.debug('start')
    time.sleep(10)
    logging.debug('end')



if __name__ == '__main__':
    # 3秒後にスレッドを走らせる
    #引数も渡せる
    t = threading.Timer(3, worker1,args=(100,),kwargs={'y':200})
    t.start()

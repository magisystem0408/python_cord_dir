"""
キュー
スレッド間で入れたり受け取ったりできる
"""

import logging
import threading
import queue
import time

logging.basicConfig(
    level=logging.DEBUG,format='%(threadName)s: %(message)s'
)

def worker1(queue):
    logging.debug('start')

    # データ挿入
    queue.put(100)
    queue.put(200)

    time.sleep(5)
    logging.debug('end')

def worker2(queue):
    logging.debug('start')

    # データ取り出し
    logging.debug(queue.get())
    logging.debug(queue.get())

    logging.debug('end')

if __name__ == '__main__':

    queue =queue.Queue()
    t1=threading.Thread(target=worker1, args=(queue,))
    t2 =threading.Thread(target=worker2, args=(queue,))

    t1.start()
    t2.start()

# 実行結果

# Thread-1: start
# Thread-2: start
# Thread-2: 100
# Thread-2: 200
# Thread-2: end
# Thread-1: end
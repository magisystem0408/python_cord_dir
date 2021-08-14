"""
キュー

・応用的使い方
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
    while True:
        item =queue.get()
        if item is None:
            break
        logging.debug(item)
        queue.task_done()

    logging.debug('########################')
    logging.debug('end')



if __name__ == '__main__':

    queue =queue.Queue()

    # タスク定義
    for i in range(10000000):
        queue.put(i)

    # スレッド複数生成
    ts =[]
    for _ in  range(10):
        t=threading.Thread(target=worker1, args=(queue,))
        t.start()
        ts.append(t)

    logging.debug('task are not done')
    queue.join()
    logging.debug('task are done')

    for _ in range(len(ts)):
        queue.put(None)

    [t.join()for t in  ts]

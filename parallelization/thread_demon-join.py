import logging
import threading
import time

"""
デーモンを入れると、
スレッドを待たずにプログラムを終了させる


joinを入れるとプログラムを待つようになる。

"""


logging.basicConfig(
    level=logging.DEBUG,
    format='%(threadName)s: %(message)s'
)

def worker1():
    logging.debug('start')
    time.sleep(10)
    logging.debug('end')


def worker2():
    logging.debug('start')
    time.sleep(3)
    logging.debug('end')


if __name__ == '__main__':
    t1 =threading.Thread(target=worker1)
    t1.setDaemon(True)
    t2 =threading.Thread(target=worker2)

    t1.start()
    t2.start()
    print('スレッドを開始しました')

    #これで必ずworker1のスレッドを待つようにする
    t1.join()
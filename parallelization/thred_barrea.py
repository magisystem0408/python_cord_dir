import logging
import threading
import time

"""
バリアは
 # スレッドが2つ立ち上がるまで次に進まない

"""


logging.basicConfig(
    level=logging.DEBUG,
    format='%(threadName)s: %(message)s'
)

def worker1(barrier):
    r =barrier.wait()
    while True:
        logging.debug('start')
        time.sleep(2)
        logging.debug('end')

def worker2(barrier):
    r =barrier.wait()
    while True:
        logging.debug('start')
        time.sleep(2)
        logging.debug('end')





if __name__ == '__main__':

    # スレッドが2つ立ち上がるまで次に進まない
    barrier =threading.Barrier(2)

    t1 =threading.Thread(target=worker1, args=(barrier,))
    t2 =threading.Thread(target=worker2, args=(barrier,))

    #ココマデマツ
    t1.start()
    t2.start()

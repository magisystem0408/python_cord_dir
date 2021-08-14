import logging
import threading
import time

"""
コンディションは
スレッドの制御をすることができる


スレッド3が先に走って終わったら
スレッド1が先に走って終わったら
スレッド2が実行される

"""


logging.basicConfig(
    level=logging.DEBUG,
    format='%(threadName)s: %(message)s'
)

def worker1(condition):
    with condition:
        condition.wait()
        logging.debug('start')
        time.sleep(2)
        logging.debug('end')

def worker2(condition):
    with condition:
        condition.wait()
        logging.debug('start')
        time.sleep(2)
        logging.debug('end')

def worker3(condition):
    with condition:
        logging.debug('start')
        time.sleep(2)
        logging.debug('end')

        ##これが発火してから残りのworker1-2が動き出す
        condition.notifyAll()



if __name__ == '__main__':
    condition =threading.Condition()

    t1 =threading.Thread(target=worker1, args=(condition,))
    t2 =threading.Thread(target=worker2, args=(condition,))
    t3 =threading.Thread(target=worker3, args=(condition,))
    t1.start()
    t2.start()
    t3.start()
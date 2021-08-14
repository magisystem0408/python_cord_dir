import logging
import threading
import time

"""
イベントは
setが押されてから他のスレッドが動き始める
"""


logging.basicConfig(
    level=logging.DEBUG,
    format='%(threadName)s: %(message)s'
)

def worker1(event):
    event.wait()
    logging.debug('start')
    time.sleep(2)
    logging.debug('end')

def worker2(event):
    event.wait()
    logging.debug('start')
    time.sleep(2)
    logging.debug('end')

def worker3(event):
    logging.debug('start')
    time.sleep(2)
    logging.debug('end')

    ##これが発火してから残りのworker1-2が動き出す
    event.set()



if __name__ == '__main__':
    event =threading.Event()

    t1 =threading.Thread(target=worker1,args=(event,))
    t2 =threading.Thread(target=worker2,args=(event,))
    t3 =threading.Thread(target=worker3,args=(event,))
    t1.start()
    t2.start()
    t3.start()
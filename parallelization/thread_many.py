import logging
import threading
import time

"""
スレッドをたくさん作る
"""


logging.basicConfig(
    level=logging.DEBUG,
    format='%(threadName)s: %(message)s'
)

def worker1():
    logging.debug('start')
    time.sleep(3)
    logging.debug('end')


if __name__ == '__main__':
    for _ in range(5):
        t =threading.Thread(target=worker1)
        t.setDaemon(True)
        t.start()

    for thread in threading.enumerate():
        if thread is threading.current_thread():
            print(thread)
            continue
        thread.join()


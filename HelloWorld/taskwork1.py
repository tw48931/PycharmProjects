#coding=utf-8
import Queue
import time
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

def start_worker():
    QueueManager.register('get_task_queue')#因为这个QueueManager只需从网络上获取Queue,所以只需要提供名字
    QueueManager.register('get_result_queue')
    server_adr = '127.0.0.1'
    print 'connecting to server %s...' % server_adr
    manager = QueueManager(address=(server_adr, 5000), authkey='abc')

    manager.connect()
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(10):
        try:
            n = task.get(timeout=1)
            print 'run task %d * %d' % (n, n)
            r = '%d * %d = %d' % (n, n, n*n)
            time.sleep(1)
            result.put(r)
        except Queue.Empty:
            print 'queue is empty.'

    print 'worker exit.'

if __name__ == '__main__':
    start_worker()



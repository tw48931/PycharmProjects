#coding=utf-8
import Queue, random, time
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

task_queue = Queue.Queue()
result_queue = Queue.Queue()

def return_task_queue():
    global task_queue
    return task_queue

def return_result_queue():
    global result_queue
    return result_queue

def start_server():
    QueueManager.register('get_task_queue', callable=return_task_queue)#关联函数名，而不是函数
    QueueManager.register('get_result_queue', callable=return_result_queue)
    manager = QueueManager(address=('127.0.0.1', 5000), authkey='abc')
    manager.start()
    task = manager.get_task_queue()#调用get_task_queue而非函数名
    result = manager.get_result_queue()
    for i in range(10):
        n = random.randint(0, 10000)
        print 'Put task %d in queue.' % n
        task.put(n)

    print 'Try to get result...'
    for i in range(10):
        try:
            r = result.get(timeout=10)
            print 'Result: %s' % r
        except Queue.Empty:
            print 'result queue is empty.'

    manager.shutdown()
    print 'manager exit.'

if __name__ == '__main__':
    start_server()
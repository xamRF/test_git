from multiprocessing import Pool
import os, time, random
from functools import wraps
import threading
#Testing

def timer(func):
    print("装饰器启动了一次")
    @wraps(func)
    def wp(*ars,**kwars):
        start=time.time()
        func(*ars,**kwars)
        end=time.time()
        print("Used %s s"%(end-start))
    return wp

@timer
def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    for i in range(1000000000):
        pass

if __name__=='__main__':
    if True:
        start_time=time.time()
        print('Parent process %s.' % os.getpid())
        p = Pool(5)
        for i in range(5):
            p.apply_async(long_time_task, args=(i,))
        print('Waiting for all subprocesses done...')
        p.close()
        p.join()
        print('All subprocesses done.')
        end_time=time.time()
        print("多进程总共用时%s"%(end_time-start_time))
    if False:
        start_time=time.time()
        long_time_task(1)
        long_time_task(2)
        long_time_task(3)
        long_time_task(4)
        long_time_task(5)
        end_time=time.time()
        print("单进程总共用时%s"%(end_time-start_time))
    if False:
        start_time=time.time()
        thread_list1=list()
        #for i in range(5):
        #    thread_list1.append(threading.Thread(target=long_time_task, args=(i,)))
        #for t in thread_list1:
        #    t.start()
        #for t in thread_list1:
        #    print(t)
        #    t.join()
        t1=threading.Thread(target=long_time_task,args=(1,))
        t2=threading.Thread(target=long_time_task,args=(2,))
        t3=threading.Thread(target=long_time_task,args=(3,))
        t4=threading.Thread(target=long_time_task,args=(4,))
        t5=threading.Thread(target=long_time_task,args=(5,))
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t5.join()
        end_time=time.time()
        print("多线程总共用时%s"%(end_time-start_time))



# -*- coding: utf-8 -*-
# CopyRight by heibanke

import time
from threading import Thread
from multiprocessing import Process

def countdown(n):
    while n > 0:
        n -= 1
        
        
COUNT = 100000000 # 1亿

def thread_process_job(n, Thread_Process, job):
    """
    n: 多线程或多进程数
    Thread_Process: Thread／Process类 
    job: countdown任务
    """
    local_time=time.time()

    #实例化多线程或多进程
    threads_or_processes = [Thread_Process(target=job,args=(COUNT//n,)) for i in xrange(n)]
    for t in threads_or_processes:
        t.start() #开始线程或进程，必须调用
    for t in threads_or_processes:
        t.join() #等待直到该线程或进程结束
    
    print n,Thread_Process.__name__," run job need ",time.time()-local_time
    

if __name__=="__main__":
    print "Multi Threads"
    for i in [1,2,4]:
        thread_process_job(i,Thread, countdown)
        
    print "Multi Process"
    for i in [1,2,4]:
        thread_process_job(i,Process, countdown)        
#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

from Queue import Queue  
import random  
import threading  
import time  
  
#生产者
class Producer(threading.Thread):  
    def __init__(self, t_name, queue):  
        threading.Thread.__init__(self, name=t_name)  
        self.data=queue  
  
    def run(self):  
        while True: 
            i = random.randint(0,10)
            self.data.put(i)  
            print "%s: %d to the queue is producted !/n" %(self.getName(), i)  
            time.sleep(0.1)  
  
#消费者
class Consumer(threading.Thread):  
    def __init__(self, t_name, queue):  
        threading.Thread.__init__(self, name=t_name)  
        self.data=queue  

    def run(self):  
        while True:
            val = self.data.get()  
            print "%s: %d in the queue is consumed!/n" %(self.getName(), val)  
            time.sleep(0.1) 
    
#主线程    
if __name__ == '__main__':  
    queue = Queue()  
    for i in range(5):
        p = Producer('Pro'+str(i), queue)  
        p.start() 
    for i in range(3):
        c = Consumer('Con'+str(i), queue)  
        c.start()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#生产与消费者模型
#当做完一个馒头后就要给顾客发送一个信号,表示已经做完,让他们吃馒头吧
import threading, time, queue
q = queue.Queue()
def Produce(name):
    count = 0   #   conut表示做的馒头总个数
    while count < 10:
        print('厨师%s在做馒头中...'%name)
        time.sleep(2)
        q.put(count)   # 容器中添加馒头
  # 当做完一个馒头后就要给顾客发送一个信号,表示已经做完,让他们吃包子
        print('produce%s已经做好了第%s个馒头'%(name, count))
        count += 1
        print('oking...')
def Consumer(name):
    count = 0    #  count表示馒头被吃的总个数
    while count < 10:
        time.sleep(2)  #  排队去取馒头
        if not q.empty():   # 如果存在
            data = q.get() #  取馒头, 吃馒头
            print('\033[32;1mConsumer %s已经把第%s个馒头吃了...\033[0m' %(name, data))
        else:
            print('馒头被吃完了...')
        count += 1
if __name__ == '__main__':
    p1 = threading.Thread(target=Produce, args=('A君',))
    c1 = threading.Thread(target=Consumer, args=('B君',))
    c2 = threading.Thread(target=Consumer, args=('C君',))
    c3 = threading.Thread(target=Consumer, args=('D君',))
    p1.start()
    c1.start()
    c2.start()
    c3.start()
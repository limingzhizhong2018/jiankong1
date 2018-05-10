import redis

import datetime
from threading import Thread

from redis.sentinel import Sentinel

sentinel = Sentinel([('127.0.0.1', 26379)], socket_timeout=0.5)

#redis 连接池，哨兵模式下不用
pool = redis.ConnectionPool(host='127.0.0.1', port=6379, password=123456)
pool2 = redis.ConnectionPool(host='127.0.0.1', port=6380, password=123456)

master = sentinel.discover_master('mymaster')
print(master)
slave = sentinel.discover_slaves('mymaster')
print(slave)


master = sentinel.master_for('mymaster', socket_timeout=0.5, password=123456)
slave = sentinel.master_for('mymaster', socket_timeout=0.5, password=123456)
x = [100, 200, 300]
z = 1
y = 0
#r = redis.Redis(connection_pool=pool)
#r2 = redis.Redis(connection_pool=pool2)

print(datetime.datetime.now())
class MyThread(Thread):
    def run(self):
        while 1:
            x = [100, 200, 300]
            z = 1
            y = 0
            y += 1
            if z == x[0]:
                print(slave.get(str(y-1)))
                print(datetime.datetime.now())
                break
            z += 1
            master.set(str(y), str(y))
    def __init__(self):
        Thread.__init__(self)

def main():
    thread_list =[]
    for i in range(1, 3):
        t = MyThread()
        thread_list.append(t)
        t.start()

if __name__ == "__main__":
    main()

#print(datetime.datetime.now())
#while True:
#    y += 1
    # print(x)
#    if x == 1000000:
 #       print(datetime.datetime.now())
#        print(slave.get(str(y-1)))
 #       break
 #   x += 1
 #   master.set(str(y), str(y))
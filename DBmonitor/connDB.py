import redis

import datetime
from threading import Thread

from redis.sentinel import Sentinel

sentinel = Sentinel([('127.0.0.1', 26379)], socket_timeout=0.5)

#redis 连接池，哨兵模式下不用
pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
pool2 = redis.ConnectionPool(host='127.0.0.1', port=6380)

#master = sentinel.discover_master('mymaster')
#print(master)
#slave = sentinel.discover_slaves('mymaster')
#print(slave)


#master = sentinel.master_for('mymaster', socket_timeout=0.5, password=123456)
#slave = sentinel.master_for('mymaster', socket_timeout=0.5, password=123456)

x = [100, 200, 300]
z = 1
y = 0
r = redis.Redis(connection_pool=pool)
r2 = redis.Redis(connection_pool=pool2)

print(datetime.datetime.now())

while 1:
    y += 1
    if z == 100:
        print(r2.get(str(y-1)))
        print(datetime.datetime.now())
        break
        z += 1
    r.set(str(y), str(y))


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
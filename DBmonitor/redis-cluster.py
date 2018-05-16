import time
import datetime
from redis import RedisError
from redis.sentinel import Sentinel
import redis
import threading

sentinel = Sentinel([('127.0.0.1', 26379)], socket_timeout=0.5)


# serverip = "127.0.0.1"
# startup_nodes = [{"host": serverip, "port": port} for port in range(6379, 6380)]
pool = redis.ConnectionPool(host='127.0.0.1', port=6381)
r = redis.Redis(connection_pool=pool)

def connRedisMaster():
    return sentinel.master_for('mymaster', socket_timeout=0.5, password=123456)


def connRedisSalve():
    return sentinel.master_for('mymaster', socket_timeout=0.5, password=123456)


try:
    def public_article(conn, article, title, user, link):
        conn.hmset(article, {'title': title, 'publicer': user, 'link': link})
except RedisError as e:
    print("".format(e))



def setRedis(x, z):
    for y in range(x, z):
        # print(str(y))
        # print(startup_nodes)
        mc = connRedisMaster()
        sc = connRedisSalve()
        try:
            r.hmset(str(y), {'title': str(y+1), 'publicer': str(y+2), 'link': str(y+3)})
        except RedisError as e:
            print("set Error".format(e), y)
        #try:
            #print(r.hgetall(str(y)).get(b'publicer'))
        #except RedisError as e:
           # print("get null".format(e), y)
    print(datetime.datetime.now())

def getRedis():

    for y in range(1, 100000):
        try:
            if r.hgetall(str(y)) == {}:
                print("该key不存在", y)
                return
        except redis.RedisError as e:
            print("该key不存在".format(e), y)


def startThread():
    t1 = threading.Thread(target=setRedis, name='getRedis', args=(1, 20000))
    t2 = threading.Thread(target=setRedis, name='getRedis', args=(20000, 40000))
    t3 = threading.Thread(target=setRedis, name='getRedis', args=(40000, 60000))
    t4 = threading.Thread(target=setRedis, name='getRedis', args=(60000, 80000))
    t5 = threading.Thread(target=setRedis, name='getRedis', args=(80000, 100001))
    print("线程1开始", datetime.datetime.now())
    t1.start()
    print("线程2开始", datetime.datetime.now())
    t2.start()
    print("线程3开始", datetime.datetime.now())
    t3.start()
    print("线程4开始", datetime.datetime.now())
    t4.start()
    print("线程5开始", datetime.datetime.now())
    t5.start()

def main():
    startThread()
    #getRedis()


if __name__ == '__main__':
    main()

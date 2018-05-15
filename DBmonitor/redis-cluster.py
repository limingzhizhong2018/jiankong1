import time

from redis import RedisError
from redis.sentinel import Sentinel

sentinel = Sentinel([('127.0.0.1', 26379)], socket_timeout=0.5)


# serverip = "127.0.0.1"
# startup_nodes = [{"host": serverip, "port": port} for port in range(6379, 6380)]

def connRedisMaster():
    return sentinel.master_for('mymaster', socket_timeout=0.5, password=123456)


def connRedisSalve():
    return sentinel.master_for('mymaster', socket_timeout=0.5, password=123456)


try:
    def public_article(conn, article, title, user, link):
        conn.hmset(article, {'title': title, 'publicer': user, 'link': link})
except RedisError as e:
    print("".format(e))


def main():
    for y in range(1, 1000000):
        print(str(y))
        # print(startup_nodes)
        mc = connRedisMaster()
        sc = connRedisSalve()
        try:
            public_article(mc, str(y), str(y + 1), str(y + 2), str(y + 3))
            time.sleep(1)
            print(sc.hgetall(str(y)).get(b'publicer'))
        except RedisError as e:
            print("".format(e))


if __name__ == '__main__':
    main()

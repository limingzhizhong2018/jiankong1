# coding=utf-8
import redis
class RedisSubscriber(object):
    """
    Redis频道订阅辅助类
    """

    def __init__(self, channel):
        self.pool = redis.ConnectionPool(host='127.0.0.1', port=6381)
        self.conn = redis.Redis(connection_pool=self.pool)
        self.channel = channel  # 定义频道名称

    def psubscribe(self):
        """
        订阅方法
        """
        pub = self.conn.pubsub()
        pub.psubscribe(self.channel)  # 同时订阅多个频道，要用psubscribe
        pub.listen()
        return pub

def test():
    subscriber = RedisSubscriber(['111', '222'])
    redis_sub = subscriber.psubscribe()  # 调用订阅方法

    while 1:
        msg = redis_sub.parse_response(block=False, timeout=60)
        print("收到订阅消息 %s" % msg)
if __name__ == '__main__':
    test()
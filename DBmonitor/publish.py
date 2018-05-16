import redis
rc = redis.Redis(host='127.0.0.1', port=6381)
ps = rc.pubsub()

def publishMessges():
    ps.subscribe(['foo'])
    while 1:
        a = input('发送消息:')
        rc.publish('222',a)
if __name__ == '__main__':
    publishMessges()
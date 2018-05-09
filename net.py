import psutil
import json
#coding:UTF-8
import requests

def get_key():

    key_info = psutil.net_io_counters(pernic=True).keys()

    recv = {}
    sent = {}

    for key in key_info:
        recv.setdefault(key, psutil.net_io_counters(pernic=True).get(key).bytes_recv)
        sent.setdefault(key, psutil.net_io_counters(pernic=True).get(key).bytes_sent)

    return key_info, recv, sent


def get_rate(func):

    import time

    key_info, old_recv, old_sent = func()

    time.sleep(1)

    key_info, now_recv, now_sent = func()

    net_in = {}
    net_out = {}

    for key in key_info:
        net_in.setdefault(key, (now_recv.get(key) - old_recv.get(key)) / 1024)
        net_out.setdefault(key, (now_sent.get(key) - old_sent.get(key)) / 1024)

    return key_info, net_in, net_out
def post(url, datas=None):
    response = requests.post(url, data=datas)
    json = response.json()
    return json

url = 'http://localhost:18088/write?db=test'
while 1:
    try:
         key_info, net_in, net_out = get_rate(get_key)



         for key in key_info:
             data = [{key:[str(net_in.get(key)),str(net_out.get(key))]}]

             json_data = json.dumps(data)
             print(json_data)
             from influxdb import InfluxDBClient
             client = InfluxDBClient('127.0.0.1', 18088, 'root', '', 'test')
             client.write_points(json_data)
             result = client.query('select value from lo0;')
             print("Result: {0}".format(result))
             #print('%s\nInput:\t %-5sKB/s\nOutput:\t %-5sKB/s\n' % (key, net_in.get(key), net_out.get(key)))

    except KeyboardInterrupt:
        exit()

from influxdb import InfluxDBClient
client = InfluxDBClient('127.0.0.1', 18088, 'root', '', 'test')
client.write_points(json_body)


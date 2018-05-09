import psutil
import datetime
from utils import db
from Entiers import SystemInfo
from influxdb.exceptions import InfluxDBClientError, InfluxDBServerError


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
        net_in.setdefault(key, (now_recv.get(key) - old_recv.get(key))/ 1024)
        net_out.setdefault(key, (now_sent.get(key) - old_sent.get(key))/ 1024)

    return key_info, net_in, net_out

key_info, net_in, net_out = get_rate(get_key)
data_net_out = []
data_net_in =[]
def getNetRx():
    for key in key_info:
        netRx = [
            {
              "measurement": "netTx",
              "tags":
                    {
                        "host": "server01",
                        "eth": key
                    },
              "fields":
                    {
                         "value": net_in.get(key),
                         "success": 1,
                   }
            }
        ]
        data_net_in.append(netRx)
    return data_net_in
def getNetTx():
    for key in key_info:
        netTx = [
            {
              "measurement": "netRx",
              "tags":
                {
                    "host": "server01",
                    "eth": key
                },
              "fields":
                {
                    "value": net_in.get(key),
                    "success": 1,
                }
            }
         ]
        data_net_out.append(netTx)
    return data_net_out
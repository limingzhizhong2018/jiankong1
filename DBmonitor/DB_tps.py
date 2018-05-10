#!/usr/bin/env python

# _*_ coding:utf-8 _*_

import MySQLdb

import datetime

import json

# qps

import time

from influxdb import InfluxDBClient

# import influxdb

try:

    conn = MySQLdb.connect(host="192.168.15.104", user="root", passwd="person", port=3306)
    client = InfluxDBClient(host=‘192.168.15.104‘, port = 8086, username ="root", password ="", database =‘telegraf‘)

    cur = conn.cursor()

    while True:

        sql = ‘‘‘show
        global status
        where
        variable_name in (‘com_select‘, ‘com_insert‘, ‘com_delete‘, ‘com_update‘, ‘com_insert_select‘, ‘uptime‘)‘‘‘

        cur.execute(sql)

        aa = cur.fetchall()

        aa = list(aa)

        delete = int(aa[0][1])

        insert1 = int(aa[1][1])

        insert2 = int(aa[2][1])

        select = int(aa[3][1])

        update = int(aa[4][1])

        uptime1 = int(aa[5][1])

        qps1 = delete + insert1 + insert2 + select + update

        time.sleep(1)

        while True:
            sql = ‘‘‘show
            global status
            where
            variable_name in (‘com_select‘, ‘com_insert‘, ‘com_delete‘, ‘com_update‘, ‘com_insert_select‘, ‘uptime‘)‘‘‘

            cur.execute(sql)

            aa = cur.fetchall()

            aa = list(aa)

            delete_2 = int(aa[0][1])

            insert_2 = int(aa[1][1])

            insert2_2 = int(aa[2][1])

            select_2 = int(aa[3][1])

            update_2 = int(aa[4][1])

            uptime2_2 = int(aa[5][1])

            qps2 = delete_2 + insert_2 + insert2_2 + select_2 + update_2

            commit = qps2 - qps1

            uptime = uptime2_2 - uptime1

        aa = (commit / uptime)

json_body = [

        {

            "measurement":my_tps,

            "tags": {

                     "host": "mycat"

                    },
            "fields": {

                 "influxdb": "qps1",

                 "qps": aa

                }

        }
]



# aa ="query_per_sec  host=mycat,role=db,influxdb=qps qps=%d "% (commit/uptime)

# aa =(commit/uptime)

# print aa,json_body


client.write_points(json_body)

break

except MySQLdb.Error, e:

print
"MySQL error%d:%s" % (e.args[0], e.args[1])

##脚本需要注意4个地方：1、连接数据库的信息，是被监控端的


json_body = [

    {

        "measurement": ‘my_tps‘,  ###注意这个红色位置不能用双引号，估计是PYTHON的问题，JAVA用双引号没问题，是个坑哦~~~！这个可以设置你喜欢的，其他不要修改，直接使用

        "tags": {

    "host": "mycat"

},

"fields": {

    "qps": aa

}

}

]
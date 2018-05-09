# - * - coding: utf-8 - * -

from influxdb import InfluxDBClient


def get_db_connection():
    db_conn = InfluxDBClient('127.0.0.1', 8086, 'root', '', 'test')
    return db_conn
from influxdb import InfluxDBClient
from hostInfo import cpu, memInof, NetRate
from influxdb.exceptions import InfluxDBClientError, InfluxDBServerError
def get_db_connection():
    db_conn = InfluxDBClient('127.0.0.1', 8086, 'root', '', 'test3')
    return db_conn
def write():
    db_conn = get_db_connection()
    cpu_point = cpu.getCpuLoad()
    mem_total_point = memInof.getMemTotal()
    mem_load_point = memInof.getMemLoad()
    mem_used_point = memInof.getMemUsed()
    net_rx_point = NetRate.getNetRx()
    net_tx_point = NetRate.getNetTx()
    try:
        db_conn.write_points(mem_load_point)
        db_conn.write_points(mem_used_point)
        db_conn.write_points(mem_total_point)
        db_conn.write_points(cpu_point)
        for index in range(len(net_rx_point)):
            db_conn.write_points(net_rx_point[index])
        for index in range(len(net_tx_point)):
            db_conn.write_points(net_tx_point[index])
    except InfluxDBClientError as e:
        print("influxdb db client error: {0}".format(e))
    except InfluxDBServerError as e:
        print("influxdb db server error: {0}".format(e))
    except Exception as e:
        print("influxdb error: {0}".format(e))
    finally:
        if db_conn is not None:
            db_conn.close()


def main():
    write()

if __name__ == '__main__':
    while 1:
        main()
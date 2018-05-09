## - * - coding: utf-8 - * -
import psutil


#获取逻辑cpu
logical_cpu= psutil.cpu_count(logical=True)
#cpu使用率
def get_rate():
    cpu =round(psutil.cpu_percent(1))
    return cpu
def getCpuLoad():
    success_point = [
                     {
                        "measurement": "cpu_load_short",
                        "tags":
                             {
                                 "host": "server01"
                             },
                        "fields":
                             {
                                 "value": get_rate(),
                                 "success": 1,
                             }
                     }
                     ]
    return success_point

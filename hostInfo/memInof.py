import psutil

def getCpuRate():
    cpu = psutil.cpu_percent(1)
    return cpu


def getMemInfo():
    mem_info = psutil.virtual_memory()
    return mem_info


def getMemTotal():
    mem_total_tmp = round(getMemInfo().total / 1024 / 1024 / 1024)
    mem_total = [
        {
            "measurement": "mem_total_short",
            "tags":
                {
                    "host": "server01"
                },
            "fields":
                {
                    "value": mem_total_tmp,
                    "success": 1,
                }
        }
    ]
    return mem_total


def getMemUsed():
    mem_used_tmp = round(getMemInfo().used / 1024 / 1024 / 1024)
    mem_used = [
        {
            "measurement": "mem_used_hort",
            "tags":
                {
                    "host": "server01"
                },
            "fields":
                {
                    "value": mem_used_tmp,
                    "success": 1,
                }
        }
    ]
    return mem_used

def getMemLoad():
    mem_load_tmp = round(round(getMemInfo().used / 1024 / 1024 / 1024) / round(getMemInfo().total / 1024 / 1024 / 1024) * 100)
    mem_load = [
        {
            "measurement": "mem_load_short",
            "tags":
                {
                    "host": "server01"
                },
            "fields":
                {
                    "value": mem_load_tmp,
                    "success": 1,
                }
        }
    ]
    return mem_load
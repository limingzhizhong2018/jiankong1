import psutil
import math

cpu_time = str(psutil.cpu_times(percpu=False))

#cpu监控

#获取逻辑cpu
logical_cpu= str(psutil.cpu_count(logical=True))
#cpu使用率
cpu = (str)(psutil.cpu_percent(1))+'%'
times = (str)(psutil.cpu_times(percpu=True))



#内存监控

mem_info =psutil.virtual_memory()
mem_total = round(mem_info.total/1024/1024)
mem_use = round(mem_info.used/1024/1024)
mem = (str)(round(mem_use/mem_total*100))


#网络监控
net_io = psutil.net_io_counters()

net_out = str(round(net_io.bytes_sent/1024/1024))
net_in = str(round(net_io.bytes_recv/1024/1024))

net = str(psutil.net_io_counters())




print(net_out)
print(net_in)
print(net)
print(cpu)
print(times)
print(mem)

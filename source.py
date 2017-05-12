from colored import fg
import os
import platform
import socket
import psutil
import cpuinfo
import calendar
import time

cpu_info = cpuinfo.get_cpu_info()
user = os.getlogin()
hostname = socket.gethostname()

os = platform.system()
version = platform.release()

cpu_usage = psutil.cpu_percent(interval=1)
cpu_count = psutil.cpu_count()
mem = psutil.virtual_memory()

disk = psutil.disk_usage('/')

# uptime snippet from: https://github.com/Bertieio/ubuntuSpecs/blob/master/UbuntuSpec.py

bootime =  psutil.boot_time()
current_time = calendar.timegm(time.gmtime())
uptime = current_time - bootime


intervals = (
    ('W', 604800),  # 60 * 60 * 24 * 7
    ('D', 86400),    # 60 * 60 * 24
    ('H', 3600),    # 60 * 60
    ('M', 60),
    ('S', 1),
    )


def display_time(seconds, granularity=4444):
    result = []

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(int(value), name))
    return ', '.join(result[:granularity])

final = display_time(uptime)

def get_info():
	
	if platform.system() == "Windows": 
		ascii_art = open("ascii\windows.txt", 'r')
		content = ascii_art.read()
		print(content.format(hostname + "@", user, os + " " + version, cpu_info['brand'], cpu_usage, cpu_count, 
			str(mem.used//(1024**2)) + "/" + str(mem.total//(1024**2)) + " MB (", str(mem.percent) + "%)", final, 
			str(disk.used//(1024**2)) + "/" + str(disk.total//(1024**2)), " MB (" + str(disk.percent) + "%)"))

get_info()


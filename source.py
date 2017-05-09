import os
import platform
import psutil

	
user = os.getlogin()
cwd = os.getcwd()
hostname = socket.gethostname()
processor = platform.processor()
system = platform.platform()
cpu_usage = psutil.cpu_percent(interval=1)
cpu_count = psutil.cpu_count()
mem = psutil.virtual_memory()

def get_info():
	
	if platform.system() == "Windows": 
		ascii_art = open("ascii\windows.txt", 'r')
		content = ascii_art.read()
		print(content.format(hostname, user, system, processor, cpu_usage, cpu_count, 
			str(mem.total//(1024**2)) + "/" + str(mem.used//(1024**2)) + " MB", mem.percent))

	

get_info()

import shutil   #Check the current available disk space

du = shutil.disk_usage("/")
print(du)

print(du.free/du.total*100)


import psutil #How much cpu is being used
print(psutil.cpu_percent(0.1))
print(psutil.cpu_percent(0.1))
print(psutil.cpu_percent(0.1))
print(psutil.cpu_percent(0.1))
print(psutil.cpu_percent(0.1))
print(psutil.cpu_percent(0.1))

print(psutil.cpu_percent(0.5))
print(psutil.cpu_percent(0.5))
print(psutil.cpu_percent(0.5))
print(psutil.cpu_percent(0.5))
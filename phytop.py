# phytop.py
# (c) Ryan Jensen 2019
#
# A visual, real-time physics-simulation with parameters controlled by all the processes running on your computer.

import psutil
for proc in psutil.process_iter():
    try:
        pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
    except psutil.NoSuchProcess:
        pass
    else:
        print(pinfo)

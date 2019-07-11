#!/usr/bin/env python2


import matplotlib.pyplot as plt
from rplidar import RPLidar
from array import *

lidar = RPLidar ('/dev/ttyUSB0')
info = lidar.get_info()
print(info)


health = lidar.get_health()
print(health)


for scan in lidar.iter_measurments():
	print(scan[0])
	print("\n")
lidar.stop()
lidar.stop_motor()
lidar.disconnect()

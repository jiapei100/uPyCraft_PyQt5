#hardware platform: pyboard V1.1

from pyb import Accel
import time

accel=Accel()           #Accel is an object that controls the accelerometer.

while True:
  time.sleep(0.1)
  print("x:%d, y:%d, z:%d"%(accel.x(),accel.y(),accel.z()))
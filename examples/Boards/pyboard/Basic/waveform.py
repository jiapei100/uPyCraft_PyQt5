#hardware platform: pyboard V1.1

from pyb import DAC,Pin
import math
import time

dac0=DAC(Pin('X5'))     
dac1=DAC(Pin('X6'))
a=0
while True:
  value=math.sin(a*math.pi/180)     #get sine
  dac0.write(int(100+value*100))    #ouput wave
  dac1.write(a*255//360)
  a+=1
  if(a==361):
    a=0
  time.sleep(0.0001)
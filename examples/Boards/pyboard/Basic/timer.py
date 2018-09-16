#hardware platform: pyboard V1.1

'''
#hardware platform: pyboard V1.1
from pyb import Timer
tim=Timer(2)
tim.init(freq=2)
tim.callback(lambda t:pyb.LED(1).toggle())
try:
  while True:
    pass
except:
  tim.deinit()
  print("timer deinit")
'''

import pyb
from pyb import LED
led=LED(1)
led.off()
def tick(timer):
  print(timer.counter())
  led.toggle()              #Toggle the LED between on and off.

tim=pyb.Timer(2,freq=2)     #create tim object,and init timer id = 2 , frequency = 2
tim.callback(tick)          #Callbacks are called every 0.5 second
try:
  while True:
    pass
except:
  tim.deinit()
  led.off()
  print("timer deinit")
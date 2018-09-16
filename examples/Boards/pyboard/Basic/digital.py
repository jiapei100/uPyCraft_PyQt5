#hardware platform: pyboard V1.1

from pyb import Pin,LED
import time

button=Pin('X1',Pin.IN)     #Create button object.
led=LED(1)                  #Create led object,id = 1
led.off()                   #turn off led

while True:
  time.sleep(1)
  if button.value()==0:
    led.off()
  else:
    led.on()
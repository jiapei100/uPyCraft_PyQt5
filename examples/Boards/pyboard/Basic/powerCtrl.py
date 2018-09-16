#hardware platform: pyboard V1.1

import pyb
from pyb import LED

led=LED(1)
led.off()

pyb.freq(168000000)         #set CPU frequency in hertz.
a=0
def blink():
  global a
  if a>8400 and a<16800:
    led.toggle()
  elif a>=16800:
    a=0
  a+=1

while True:
  blink()
  pyb.wfi()                 #pyb.wfi() is used to reduce power consumption while waiting for an event such as an interrupt. 
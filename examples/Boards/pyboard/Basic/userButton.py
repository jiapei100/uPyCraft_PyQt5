#hardware platform: pyboard V1.1

from pyb import Switch
from pyb import LED

def mycallback():
  led.toggle()              #Toggle the LED between on and off.

led=LED(1)
led.off()
userButton=Switch()         #Create and return a switch object.

#userButton.callback(lambda:led.toggle())
userButton.callback(mycallback)

while True:
  pass
#hardware platform: pyboard V1.1

import pyb
import time

s1=pyb.Servo(1)     # create a servo object on position X1
s2=pyb.Servo(2)

s1.angle(45)        # move servo1 to 45 degrees
s2.angle(0)
time.sleep(1.5)

# move servo1 and servo2 synchronously, taking 1500ms
s1.angle(-60,1500)
s2.angle(30,1500)

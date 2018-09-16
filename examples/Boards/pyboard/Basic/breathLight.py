#hardware platform: pyboard V1.1

from pyb import Timer
from time import sleep
import pyb
tim=pyb.Timer(5,freq=100)                                               #create Timer object
tchannel=tim.channel(1,Timer.PWM,pin=pyb.Pin.board.X1,pulse_width=0)    #init and return a timer channel object
                                                                        #configure the timer in PWM mode and initial pulse width value
max_width=50000
min_width=100
wstep=1500
cur_width=min_width
while True:                                                             #change pulse width between 100 and 50000
  tchannel.pulse_width(cur_width)                                       #set pulse width
  sleep(0.1)
  cur_width+=wstep
  if cur_width>max_width:
    cur_width=max_width
    wstep *=-1
  elif cur_width<min_width:
    cur_width=min_width
    wstep*=-1
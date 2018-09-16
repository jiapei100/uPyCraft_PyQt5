#Hardware Platform: FireBeetle-ESP32
#Result: IO25 output sin wave, IO26 output cos wave.
#Hardware Connection: IO25 and IO26 need to  be connected to an oscilloscope if waveform observation is needed. 
#The info below shows that waveform is available for the current version.
# IO25  IO26
#FireBeetle-ESP32 has 2 DAC signal pins in all.

from machine import DAC,Pin
import math
import time

dac0=DAC(Pin(25))
dac1=DAC(Pin(26))
a=0
while True:
  value=math.sin(a*math.pi/180)         #get sine
  dac0.write(int(100+value*100))        #ouput wave
  dac1.write(a*255//360)
  a+=1
  if(a==361):
    a=0
  time.sleep(0.0001)

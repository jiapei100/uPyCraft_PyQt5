#Hardware Platform: FireBeetle-ESP32
#Result: measure enviromental temperature.
#Hardware Connection: this test need to connect a 'DS18B20' digital temperature sensor in IO25.
#The info below shows that ds18b20Demo is available for the current version. 
# IO0  IO2  IO4  IO5  IO9  IO10 IO12~19 
# IO21 IO22 IO23 IO25 IO26 IO27 

from machine import Pin
import onewire
import ds18x20
import time

ow = onewire.OneWire(Pin(25))   #Init wire
ow.scan()
ds=ds18x20.DS18X20(ow)          #create ds18x20 object
while True:
  roms=ds.scan()                #scan ds18x20
  ds.convert_temp()             #convert temperature
  for rom in roms:
    print(ds.read_temp(rom))    #display 
  time.sleep(1)


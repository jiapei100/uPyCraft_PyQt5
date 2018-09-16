#hardware platform: FireBeetle-ESP8266

from machine import ADC
import time

adc0=ADC(0)                     #create ADC object on ADC pin

while True:
  print("adc0=",adc0.read())    #read value, 0-1024
  time.sleep(0.1)
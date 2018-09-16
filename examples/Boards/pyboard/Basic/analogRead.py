#hardware platform: pyboard V1.1
from pyb import ADC,Pin
import time

adc0=ADC(Pin('X19'))
adc1=ADC(Pin('X20'))
adc2=ADC(Pin('X21'))
adc3=ADC(Pin('X22'))

while True:
  print("adc0=",adc0.read())
  print("adc1=",adc1.read())
  print("adc2=",adc2.read())
  print("adc3=",adc3.read())
  time.sleep(0.1)
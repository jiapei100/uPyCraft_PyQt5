#Hardware Platform: FireBeetle-ESP32
#Result: measure enviromental temperature.
#Hardware Connection: this test need to connect a 'MLX90614' IR(infrared) temperature sensor in IO25.
#The info below shows that MLX90614Demo is available for the current version.  
# IO0  IO2  IO4  IO5  IO9  IO10  IO21~23  IO25~27

import MLX90614
from machine import Pin,I2C
import time

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=100000)    #create I2C object,init I2C
ir=MLX90614.MLX90614(i2c)                           #create ir object,and transmit the i2c object to it

while True:
  time.sleep(1)
  print("Object  %s *C"% ir.getObjCelsius())        #print celsius of Object
  print("Object  %s *F"% ir.getObjFahrenheit())     #print fahrenheit of Object
  print("Ambient %s *C"% ir.getEnvCelsius())        #print celsius of Ambient
  print("Ambient %s *F"% ir.getEnvFahrenheit())     #print fahrenheit of Ambient
  print()

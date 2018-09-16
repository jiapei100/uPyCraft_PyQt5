import sys
from machine import I2C
from micropython import const

MLX90614_IIC_ADDR   = const(0x5A)
MLX90614_TA         = const(0x06)
MLX90614_TOBJ1      = const(0x07)

class MLX90614:
  def __init__(self,i2c,addr=MLX90614_IIC_ADDR):
    self.addr=addr
    self.i2c=i2c

  def getObjCelsius(self):
    return self.getTemp(MLX90614_TOBJ1)	#Get celsius temperature of the object 

  def getEnvCelsius(self):
    return self.getTemp(MLX90614_TA)    #Get celsius temperature of the ambient

  def getObjFahrenheit(self):
    return (self.getTemp(MLX90614_TOBJ1) * 9 / 5) + 32  #Get fahrenheit temperature of the object

  def getEnvFahrenheit(self):
    return (self.getTemp(MLX90614_TA) * 9 / 5) + 32 #Get fahrenheit temperature of the ambient

  def getTemp(self,reg):
    temp = self.getReg(reg)*0.02-273.15             #Temperature conversion
    return temp

  def getReg(self,reg):
    data = self.i2c.readfrom_mem(self.addr,reg,3)               #Receive DATA
    result = (data[1]<<8) | data[0]
    return result




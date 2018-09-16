#hardware platform:FireBeetle-ESP32

from machine import Pin,I2C
import time

i2c = I2C(scl=Pin(22),sda=Pin(21), freq=10000)  #create I2C object,init Pin and frequency
b=bytearray("dfrobot")                          #create a array
i2c.writeto_mem(0x50,0,b,addrsize=16)           #Write b to the slave specified by 0x50 starting 
                                                #from the memory address specified by 0, The addrsize is 16
time.sleep(0.1)
print(i2c.readfrom_mem(0x50,0,7,addrsize=16))   #Read 7 bytes from the slave specified by 0x50 starting from the memory address specified by 0. 
                                                #The addrsize specifies the address size in bits. Returns a bytes object with the data read.

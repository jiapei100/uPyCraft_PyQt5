#Hardware Platform: FireBeetle-ESP32
#Result: measure distance of 20-750cm and temperature.
#Hardware Connection: this test need to connect a 'URM07'  sensor by serial port communication of IO25(RX) and IO26(TX).
#The info below shows that urm07Demo is available for the current version. 
# IO0   IO2  IO4  IO5  IO9  IO10  IO25
# IO26  IO39 IO12~19  IO21~23  IO34~36 

from machine import UART
import urm07
import time

u2 = UART(2,baudrate=19200,rx=25,tx=26,timeout=10)  #create UART object,init id,baudrate,tx,rx,timeout
time.sleep(1)

urm = urm07.URM07(u2,interval=200)                  #create URM07 object,,and transmit the i2c object to it,set interval
#urm.setDeviceAddr(0x11)
#urm.setBaudRate(urm07.BAUDRATE19200)
while True:
  distance = urm.getDistance()                      #get the distance from urm
  if(distance == 65535):
    print("measure distance failure!!!")
  else:
    print("distance=%d mm"%distance)
  print("temp=%3.1f C"%(urm.getTemperature()/10))   #get the temprature from urm,the integer is 3 bits,and the float is 1 bit
  
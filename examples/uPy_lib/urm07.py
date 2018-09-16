from micropython import const
import time
import sys
import struct

BAUDRATE1200   = const(0)
BAUDRATE2400   = const(1)
BAUDRATE4800   = const(2)
BAUDRATE9600   = const(3)
BAUDRATE14400  = const(4)
BAUDRATE19200  = const(5)
BAUDRATE28800  = const(6)
BAUDRATE38400  = const(7)
BAUDRATE57600  = const(8)
BAUDRATE115200 = const(9)
BAUDRATE128000 = const(10)
BAUDRATE216000 = const(11)

CMD_GETDIS     = const(0x02)
CMD_GETTEMP    = const(0x03)
CMD_SETADDR    = const(0x55)
CMD_SETBAUD    = const(0x08)

class URM07:
  def __init__(self,uart,addr=0x11,interval=200):
    self.uart = uart
    self.addr = addr
    self.interval = interval
  def sendAndResponse(self,cmd):
    sum = 0
    for x in cmd:
      sum += x
    cmd.append(sum&0xff)
    self.uart.write(cmd)
    time.sleep_ms(self.interval)
    resp = self.uart.read()
    return resp
  def getDistance(self):
    cmd= bytearray(struct.pack('5B',0x55,0xaa,self.addr,0,CMD_GETDIS))
    resp = self.sendAndResponse(cmd)
    print(resp)
    dis = resp[5]*256+resp[6]
    return dis
  def getTemperature(self):
    cmd = bytearray(struct.pack('5B',0x55,0xaa,self.addr,0,CMD_GETTEMP))
    resp = self.sendAndResponse(cmd)
    temp = resp[5]*256+resp[6]
    return temp
  def setDeviceAddr(self,newAddr):
    cmd= bytearray(struct.pack('6B',0x55,0xaa,0xAB,1,CMD_SETADDR,newAddr))
    resp = self.sendAndResponse(cmd)
    if(resp[5] == 0xCC):
      self.addr = newAddr
      return True
    else:
      return False
  def setBaudRate(self,baudrate):
    cmd= bytearray(struct.pack('6B',0x55,0xaa,self.addr,1,CMD_SETBAUD,baudrate))
    resp = self.sendAndResponse(cmd)
    if(resp[5] == 0xCC):
      return True
    else:
      return False
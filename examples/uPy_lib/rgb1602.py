import time
import sys
from micropython import const

currentBoard=""
if(sys.platform=="esp8266"):
  currentBoard="esp8266"
elif(sys.platform=="esp32"):
  currentBoard="esp32"
elif(sys.platform=="pyboard"):
  currentBoard="pyboard"

LCD_FUNCTIONSET         = const(0x20)
LCD_CLEARDISPLAY        = const(0x01)
LCD_RETURNHOME          = const(0x02)
LCD_CURSORSHIFT         = const(0x10)
LCD_2LINE               = const(0x08)
LCD_DISPLAYON           = const(0x04)
LCD_DISPLAYCONTROL      = const(0x08)
LCD_CURSOROFF           = const(0x00)
LCD_BLINKOFF            = const(0x00)
LCD_ENTRYMODESET        = const(0x04)
LCD_ENTRYLEFT           = const(0x02)
LCD_ENTRYSHIFTDECREMENT = const(0x00)

LCD_DISPLAYMOVE         = const(0x08)
LCD_CURSORMOVE          = const(0x00)
LCD_MOVERIGHT           = const(0x04)
LCD_MOVELEFT            = const(0x00)

REG_MODE1               = const(0x00)
REG_MODE2               = const(0x01)
REG_OUTPUT              = const(0x08)
REG_RED                 = const(0x04)
REG_GREEN               = const(0x03)
REG_BLUE                = const(0x02)

class LCD:
  def __init__(self, row, col):
    self._row = row
    self._col = col
    print("LCD _row=%d _col=%d"%(self._row,self._col))

  def print(self,arg):
    if(isinstance(arg,int)):
      arg=str(arg)

    for x in bytearray(arg):
      self.write(x)

class RGB1602(LCD):
  def __init__(self, col, row, i2c):
    self.i2c=i2c
    super().__init__(row, col)
    for cmd in(
    LCD_FUNCTIONSET | LCD_2LINE,
    LCD_DISPLAYCONTROL | LCD_DISPLAYON | LCD_CURSOROFF | LCD_BLINKOFF,
    LCD_CLEARDISPLAY,
    LCD_ENTRYMODESET | LCD_ENTRYLEFT | LCD_ENTRYSHIFTDECREMENT
    ):
      self.command(cmd)
      time.sleep(0.1)
    self.setReg(REG_MODE1, 0)
    self.setReg(REG_OUTPUT, 0xFF)
    self.setReg(REG_MODE2, 0x20)
        
  def command(self,cmd):
    b=bytearray(2)
    b[0]=0x80
    b[1]=cmd
    global currentBoard
    if currentBoard=="esp8266" or currentBoard=="esp32":
      self.i2c.writeto(62,b)
    elif currentBoard=="pyboard":
      self.i2c.send(b,62)

  def write(self,data):
    b=bytearray(2)
    b[0]=0x40
    b[1]=data
    global currentBoard
    if currentBoard=="esp8266" or currentBoard=="esp32":
      self.i2c.writeto(62,b)
    elif currentBoard=="pyboard":
      self.i2c.send(b,62)
    
  def setReg(self,reg,data):
    b=bytearray(1)
    b[0]=data
    global currentBoard
    if currentBoard=="esp8266" or currentBoard=="esp32":
      self.i2c.writeto_mem(96,reg,b)
    elif currentBoard=="pyboard":
      self.i2c.mem_write(b,96,reg)

  def setRGB(self,r,g,b):
    self.setReg(REG_RED,  r)
    self.setReg(REG_GREEN,  g)
    self.setReg(REG_BLUE,  b)
  def setCursor(self,col,row):
    if(row == 0):
      col|=0x80
    else:
      col|=0xc0;
    self.command(col)
  def clear(self):
    self.command(LCD_CLEARDISPLAY)
    time.sleep_ms(2)
  def scrollDisplayLeft(self):
    self.command(LCD_CURSORSHIFT | LCD_DISPLAYMOVE | LCD_MOVELEFT)
  def scrollDisplayRight(self):
    self.command(LCD_CURSORSHIFT | LCD_DISPLAYMOVE | LCD_MOVERIGHT)

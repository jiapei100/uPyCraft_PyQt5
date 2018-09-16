from machine import Pin
import framebuf
from micropython import const

DFROBOT_HT1632_READ = const(0x06)
DFROBOT_HT1632_WRITE = const(0x05)
DFROBOT_HT1632_COMMAND = const(0x04)
DFROBOT_HT1632_SYS_DIS = const(0x00)
DFROBOT_HT1632_SYS_EN = const(0x01)
DFROBOT_HT1632_LED_OFF = const(0x02)
DFROBOT_HT1632_LED_ON = const(0x03)
DFROBOT_HT1632_BLINK_OFF = const(0x08)
DFROBOT_HT1632_BLINK_ON = const(0x09)
DFROBOT_HT1632_SLAVE_MODE = const(0x10)
DFROBOT_HT1632_MASTER_MODE = const(0x14)
DFROBOT_HT1632_INT_RC = const(0x18)
DFROBOT_HT1632_EXT_CLK = const(0x1C)
DFROBOT_HT1632_PWM_CONTROL = const(0xA0)
DFROBOT_HT1632_COMMON_8NMOS = const(0x20)
DFROBOT_HT1632_COMMON_16NMOS = const(0x24)
DFROBOT_HT1632_COMMON_8PMOS = const(0x28)
DFROBOT_HT1632_COMMON_16PMOS = const(0x2C)

class HT1632C():
  def __init__(self,DATA,CLK,CS):
    self.width = 240
    self.height = 8
    self.CS = Pin(CS,Pin.OUT)
    self.DATA = Pin(DATA,Pin.OUT)
    self.CLK = Pin(CLK,Pin.OUT)
    self.CS.value(1)
    self.pages = self.height // 8
    self.buffer = bytearray(self.pages * self.width)
    self.framebuf = framebuf.FrameBuffer(self.buffer, self.width, self.height, framebuf.MVLSB)
    self.begin()
  def begin(self):
    for cmd in (
      DFROBOT_HT1632_SYS_EN,
      DFROBOT_HT1632_LED_ON,
      DFROBOT_HT1632_BLINK_OFF,
      DFROBOT_HT1632_MASTER_MODE,
      DFROBOT_HT1632_INT_RC,
      DFROBOT_HT1632_COMMON_16NMOS,
      DFROBOT_HT1632_PWM_CONTROL | 0xF
    ):
      self.writeCommand(cmd)

  def writeCommand(self, cmd):
    val = (DFROBOT_HT1632_COMMAND<<9) | (cmd <<1)
    self.CS.value(0)
    self.writeBits(val,12)
    self.CS.value(1)

  def show(self):
    self.CS.value(0)
    self.writeBits(DFROBOT_HT1632_WRITE,3)
    self.writeBits(0,7)
    for i in range(24):
      val = self.buffer[23-i]
      val <<= 8
      self.writeBits(val,16)
    self.CS.value(1)


  def writeBits(self,data,length):
    while length:
      self.CLK.value(0)
      if(data & (1<< length-1)):
        self.DATA.value(1)
      else:
        self.DATA.value(0)
      self.CLK.value(1)
      length-=1

  def fill(self, col):
    self.framebuf.fill(col)
  def pixel(self, x, y, col):
    self.framebuf.pixel(x, y, col)
  def scroll(self, dx, dy):
    self.framebuf.scroll(dx, dy)
  def text(self, string, x, y, col=1):
    self.framebuf.text(string, x, y, col)
  def hline(self, x, y, w, col):
    self.framebuf.hline(x, y, w, col)
  def vline(self, x, y, h, col):
    self.framebuf.vline(x, y, h, col)
  def line(self, x1, y1, x2, y2, col):
    self.framebuf.line(x1, y1, x2, y2, col)
  def rect(self, x, y, w, h, col):
    self.framebuf.rect(x, y, w, h, col)
  def fill_rect(self, x, y, w, h, col):
    self.framebuf.fill_rect(x, y, w, h, col)
  def blit(self, fbuf, x, y):
    self.framebuf.blit(fbuf, x, y)

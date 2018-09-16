from microbit import *

try:
  while True:
    if pin0.is_touched():
      display.show(Image.HAPPY)
    else:
      display.show(Image.SAD)
except:
  display.clear()
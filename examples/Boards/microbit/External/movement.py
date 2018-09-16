from microbit import *

while True:
  reading = accelerometer.get_x()
  if reading > 30:
    display.show("R")
  elif reading < -30:
    display.show("L")
  else:
    display.show("-")
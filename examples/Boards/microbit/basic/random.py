from microbit import *
import random

try:
  while True:
    display.scroll(str(random.randint(1, 6)))
except:
  display.clear()
'''
from microbit import *
import random

while True:
  if button_a.is_pressed():
    display.scroll(str(random.randint(1, 6)))
'''
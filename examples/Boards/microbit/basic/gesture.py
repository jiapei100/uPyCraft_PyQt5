
#demo1
from microbit import *

while True:
  gesture = accelerometer.current_gesture()
  if gesture == "face up":
    display.show(Image.HAPPY)
  else:
    display.show(Image.ANGRY)


'''
#demo2
from microbit import *
import random
a = ["a","b","c"]
while True:
  if accelerometer.is_gesture("shake"):
    display.scroll(random.choice(a))
'''
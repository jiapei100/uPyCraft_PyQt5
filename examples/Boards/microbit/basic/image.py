#demo1from microbit import displayfrom microbit import sleepfrom microbit import Imagetry:  while True:    display.show(Image.HAPPY)    sleep(1000)    display.clear()    sleep(1000)except:  display.clear()'''#demo2from microbit import displayfrom microbit import Imagefrom microbit import sleepImage1=Image("99999:80000:77777:00006:55555")#show the number "5",the value of light 0-9try:  while True:    display.show(Image1)    sleep(1000)    display.clear()    sleep(1000)except:  display.clear()''''''#demo3
from microbit import display
from microbit import sleep
from microbit import Image

Image1=Image("99999:80000:77777:00006:55555")#show the number "5",the value of light 0-9
mixed_list = [Image1, Image.HAPPY]

try:
  display.show(mixed_list, loop=True, delay=1000)
except:
  display.clear()'''
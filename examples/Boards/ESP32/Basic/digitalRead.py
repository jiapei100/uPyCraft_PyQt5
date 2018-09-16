#hardware platform: FireBeetle-ESP32

from machine import Pin
import time

button=Pin(27,Pin.IN)           #create Button object from pin27,Set Pin27 to input (D4)
led=Pin(25,Pin.OUT)             #create LED object from pin25,Set Pin25 to output (D2)

while True:
  led.value(button.value())     #Gets Button state and passes the state to LED
  time.sleep(0.1)

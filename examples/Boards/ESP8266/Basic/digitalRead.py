#hardware platform: FireBeetle-ESP8266

from machine import Pinimport time
button=Pin(15,Pin.IN)           #create Button object from pin15,Set Pin15 to input (D4)led=Pin(13,Pin.OUT)             #create LED object from pin13,Set Pin13 to output (D2)
while True:  led.value(button.value())     #Gets the state of the Button and passes the state to the LED  time.sleep(0.1)
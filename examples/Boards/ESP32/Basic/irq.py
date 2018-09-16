#Hardware Platform: FireBeetle-ESP32#Result: button controls LED ON/OFF.   #Hardware Connection: this test needs to connect to an external button module in IO27 and an external LED module in IO25. #The info below shows that irq is available for the current version.# button:IO2  IO4  IO5  IO10 IO12~19 IO23 IO25#        IO26 IO27 IO34 IO35 IO36    IO39# led:   IO0  IO4  IO10 IO12~19  IO21~23 IO25~27#Except the connection between IO2 and onboard LED, other pins need to connect to external LEDs.
from machine import Pinimport timeimport machine
value=1
counter=0
def func(v):
  global value,counter
  time.sleep_ms(50)  if(button.value() == 0):                          #When the button is not pressed, return    return  while(button.value() == 1):                       #If press the button, it will wait until released    time.sleep_ms(100)  time.sleep_ms(100)  counter+=1  led.value(value)                                  #Set LED value
  value = 0 if value else 1                         #If LED is turn on,it will be shutdown next,otherwise if will turn on next.
  print("IRQ ",counter)
try:
  led = Pin(25, Pin.OUT)                              #create LED object from pin25,Set Pin25 to output
  led.value(0)
  button = Pin(27, Pin.IN)                            #create Button object from pin27,Set Pin27 to input
  button.irq(trigger=Pin.IRQ_RISING, handler=func)    #init irq,set interrupt on rising edge,and callback function is func
  while True:
    passexcept:  machine.disable_irq()
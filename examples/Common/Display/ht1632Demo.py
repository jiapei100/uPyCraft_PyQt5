#hardware platform: FireBeetle-ESP8266

import ht1632

DATAPIN=5
CLKPIN =4
CSPIN  =13

led=ht1632.HT1632C(DATAPIN,CLKPIN,CSPIN,24,8)       #create LED object,and bind data pin,clk pin,cs pin
led.text("DFR",0,0)                                 #set "DFR" at (0,0)
led.show()                                          #display String

while True:
  led.scroll(-1,0)                                  #Shift the contents of the String by the given vector.
  led.show()
  time.sleep(0.5)
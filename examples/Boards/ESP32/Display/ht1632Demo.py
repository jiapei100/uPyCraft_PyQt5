#hardware platform: FireBeetle-ESP32
import ht1632
import time

DATAPIN=10
CLKPIN =13
CSPIN  =25

led=ht1632.HT1632C(DATAPIN,CLKPIN,CSPIN)

while True:
  led.fill(0)
  led.text("DFR",0,0,1)
  
  led.hline(26,3,15,1)
  led.line(33,0,41,3,1)
  led.line(33,6,41,3,1)
  led.rect(43,0,24,8,1)
  led.show()

  for i in range(43):
    led.scroll(-1,0)
    led.show()
    time.sleep(0.1)
    
  led.fill_rect(2,2,9,4,1)
  led.show()
  for j in range(2,6):
    for i in range(13,22):
      led.pixel(i,j,1)
      led.show()
  time.sleep(5)
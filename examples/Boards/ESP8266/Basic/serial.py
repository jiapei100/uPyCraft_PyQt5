#hardware platform: FireBeetle-ESP8266
from machine import UART
uart=UART(0)                #create uart object and init
uart.write("dfrobot\r\n")   #write the string "dfrobot"
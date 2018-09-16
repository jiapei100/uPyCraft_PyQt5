#hardware platform: pyboard V1.1
#uart1:tx->x9,rx->x10

from pyb import UART

uart=UART(1,9600)       #init with given baudrate
uart.write("hello")     #write "hello"
msg=""
while True:
  msg=uart.read(5)      # read 5 characters, returns a bytes object 
  if msg!=None:
    break
print(msg)
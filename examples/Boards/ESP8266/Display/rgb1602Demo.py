from machine import Pin,I2C
import rgb1602
import time

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)      #Init i2c

print("========DFRobot ESP8266 I2C LCD1602 TEST===========")
lcd=rgb1602.RGB1602(16,2,i2c)                       #create LCD object,Specify col and row
lcd.setRGB(0,50,0);                                 #set the value of RGB
lcd.setCursor(0,0)                                  #set the value of coordinates
lcd.print("DFRobot")                                #display "DFRobot"

lcd.setCursor(5,1)
lcd.print("chengdu")
#lcd.home()
lcd.print(3322)
while True:
  time.sleep(1)
  lcd.scrollDisplayLeft()                         #Set the display mode and scroll direction
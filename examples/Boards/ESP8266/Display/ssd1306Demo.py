#hardware platform: FireBeetle-ESP8266from machine import Pin,I2C
import ssd1306
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)  #Init i2c
lcd=ssd1306.SSD1306_I2C(128,64,i2c)             #create LCD object,Specify col and row
lcd.text("DFRobot",0,0)                         #set "DFRobot" at (0,0)
lcd.text("chengdu",24,16)                       #set "chengdu" at (24,16)
lcd.text("123456",64,24)                        #set "123456" at (64,24)
lcd.show()                                      #display
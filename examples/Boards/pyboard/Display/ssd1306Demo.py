#hardware platform: pyboard V1.1

import pyb
import ssd1306

i2c=pyb.I2C(1,pyb.I2C.MASTER,baudrate=100000)   #Init i2c
lcd=ssd1306.SSD1306_I2C(128,64,i2c)             #create LCD object,Specify width and height
lcd.text("DFRobot",0,0)                         #set "DFRobot" at (0,0)
lcd.text("chengdu",24,16)                       #set "chengdu" at (24,16)
lcd.text("123456",64,24)                        #set "123456" at (64,24)
lcd.show()                                      #display
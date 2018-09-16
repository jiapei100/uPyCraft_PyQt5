#hardware platform: FireBeetle-ESP32

from machine import Pin,I2C
import ssd1306
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=100000)
lcd=ssd1306.SSD1306_I2C(128,64,i2c)

lcd.text("DFRobot",0,0)
for i in range(0,28):
  lcd.pixel(2*i,10,1)

lcd.line(0,12,54,12,1)              #draw a line from (0,12) to (54,12) color is blue
lcd.hline(10,32,108,1)              #draw a horizontal line,from (10,32),length 108,color is blue
lcd.vline(64,0,64,1)                #draw a vertical line,from (64,0),length 64,color is blue
lcd.fill_rect(59,27,10,10,1)        #draw a rectangle,from (59,27) to (10,10) fill with blue
lcd.rect(56,24,16,16,1)             #draw a rectangle frame,from (59,27) to (10,10) and color is blue
lcd.fill_rect(59,27,10,10,1)
lcd.fill_rect(88,0,40,20,1)
lcd.line(88,0,128,20,0)             #draw a line from (88,0) to (128,20) color is black
lcd.line(88,20,128,0,0)
lcd.show()                          #display pix
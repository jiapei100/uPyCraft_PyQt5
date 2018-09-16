#hardware platform: FireBeetle-ESP8266
from machine import RTC
import time
rtc = RTC()                             #create RTC object
print(rtc.datetime())                   #print time(year, month, day, hour, minute, second, microsecond, tzinfo)
#rtc.datetime((2017,5,20,5,0,0,0,0))    #you can use this to set current time
print(rtc.datetime())
time.sleep(3.5)
print(rtc.datetime())
print(rtc.memory())                     #print the memory of rtc
rtc.memory("dfrobot"+str(rtc.datetime()[6]))    #set rtc memory

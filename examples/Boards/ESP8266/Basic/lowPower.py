#hardware platform: FireBeetle-ESP8266

import machine
import time

rtc = machine.RTC()                 #create RTC object
rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)     #Create an irq object triggered by a real time clock alarm.

if machine.reset_cause() == machine.DEEPSLEEP_RESET:    #judge the reset cause.
  print('woke from a deepsleep')
print("deepsleep 3 seconds")
rtc.alarm(rtc.ALARM0, 3000)         #Set the RTC alarm,wake up in three seconds
machine.deepsleep()                 #let board deepsleep

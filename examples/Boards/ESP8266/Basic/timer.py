#hardware platform: FireBeetle-ESP8266

from machine import Timer,RTC

rtc=RTC()
tim0 = Timer(-1)    #Construct a new timer object of the given id. Id of -1 constructs a virtual timer
tim1 = Timer(-1)

#tim0 init,Call the callback function to display the string one time with three seconds later
tim0.init(period=3000, mode=Timer.ONE_SHOT, callback=lambda t:print("performing at the first 3 seconds once, timestamp:"+str(rtc.datetime())))

#tim1 init,Calls the callback function to display the string per second
tim1.init(period=1000, mode=Timer.PERIODIC, callback=lambda t:print("performing period=1s, timestamp: "+str(rtc.datetime())))

#Catch exceptions,stop program if interrupted accidentally in the 'try'
try:
  while True:
    pass
except:
  tim0.deinit()
  tim1.deinit()